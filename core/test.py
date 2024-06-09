import cavablar_dirnaq_list as cb
import db as d
import os
import csvtodict as csvdict

replaceletter = {
    "e": "Ə",
    "s": "Ş",
    "u": "Ü",
    "g": "Ğ",
}


def get_file_path(prompt, directories_to_check=None):
    if directories_to_check is None:
        directories_to_check = [os.getcwd(), os.path.join(os.getcwd(), 'core'), os.path.join(os.getcwd(), 'txt')]

    while True:
        file_name = input(prompt)
        for directory in directories_to_check:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                return file_path
        print("Fayl tapılmadı.")


def read_and_replace(filepath, replace_dict):
    try:
        with open(filepath, "r", encoding="utf8") as file:
            content = file.read()
        for key, value in replace_dict.items():
            content = content.replace(key, value)
        return content
    except FileNotFoundError:
        print(f"Fayl tapılmadı: {filepath}")
        return ""


def initialize_variables(sinaq_info):
    variables = {
        'fenncavabdeyisenler': {},
        'duzguncavabdeyisenler': {},
        'fennduzdeyisenler': {},
        'fennsehvdeyisenler': {},
        'fennsualsaydeyisenler': {},
        'fennbaldeyisenler': {},
        'fenncembaldeyisenler': {},
        'fennaddeyisenler': {}
    }

    cavabstartcoordinate = 0
    fenncoordinate = [64]

    for j in range(1, int(sinaq_info["fenn_sayi"]) + 1):
        fenn_no = f"fenn{j}"
        variables['fenncavabdeyisenler'][fenn_no] = ""

        fenn_no_duz = f"fenn_{j}_duz"
        variables['fennduzdeyisenler'][fenn_no_duz] = 0

        fenn_no_sehv = f"fenn_{j}_sehv"
        variables['fennsehvdeyisenler'][fenn_no_sehv] = 0

        fenn_sual_say_deyisen = f"fennsual{j}"
        variables['fennsualsaydeyisenler'][fenn_sual_say_deyisen] = sinaq_info[fenn_sual_say_deyisen]

        fenn_bal_deyisen = f"fennbal{j}"
        variables['fennbaldeyisenler'][fenn_bal_deyisen] = sinaq_info[fenn_bal_deyisen]

        fenn_ad_deyisen = f"fennad{j}"
        variables['fennaddeyisenler'][fenn_ad_deyisen] = sinaq_info[fenn_ad_deyisen]

        fenn_cem_bal_deyisen = f"fenn{j}_bal"
        variables['fenncembaldeyisenler'][fenn_cem_bal_deyisen] = 0

        duzguncavab_no = f"dzgn_cvb_f{j}"
        duzguncavabcoordinate = cavabstartcoordinate + int(variables['fennsualsaydeyisenler'][fenn_sual_say_deyisen])
        variables['duzguncavabdeyisenler'][duzguncavab_no] = cb.dzgn_cvb(cavabstartcoordinate, duzguncavabcoordinate)
        cavabstartcoordinate += int(variables['fennsualsaydeyisenler'][fenn_sual_say_deyisen])
        fenncoordinate.append(fenncoordinate[-1] + int(variables['fennsualsaydeyisenler'][fenn_sual_say_deyisen]))

    return variables, fenncoordinate


def process_student_results(dosya_list, variables_template, fenncoordinate, sehvduz, sehvduzsay):
    for z in range(len(dosya_list)):
        variables = {key: value.copy() for key, value in variables_template.items()}  # Reset variables for each student
        student_info = extract_student_info(dosya_list[z])
        total_score = 0

        for x in range(1, len(fenncoordinate)):
            update_fenncavabdeyisenler(variables, dosya_list[z], x, fenncoordinate)
            if len(variables['fenncavabdeyisenler'][f"fenn{x}"]) == int(
                    variables['fennsualsaydeyisenler'][f"fennsual{x}"]):
                calculate_scores(variables, x, sehvduz, sehvduzsay)
                total_score += variables['fenncembaldeyisenler'][f"fenn{x}_bal"]

        total_score = round(total_score, 2)

        d.db_third(*student_info, total_score, variables['fennduzdeyisenler'],
                   variables['fennsehvdeyisenler'], variables['fenncembaldeyisenler'],
                   variables['fenncavabdeyisenler'], variables['duzguncavabdeyisenler'],
                   variables['fennaddeyisenler'])


def extract_student_info(dosya_line):
    ad = dosya_line[0:12].strip()
    soyad = dosya_line[13:25].strip()
    is_no = dosya_line[26:33].strip()
    ata_adi = dosya_line[37:49].strip()
    cins = 'Kişi' if dosya_line[54:55] == 'K' else 'Qadın' if dosya_line[54:55] == 'Q' else ' '
    sinif = dosya_line[58:59].strip()
    return ad, soyad, is_no, ata_adi, cins, sinif


def update_fenncavabdeyisenler(variables, dosya_line, x, fenncoordinate):
    fenn_key = f"fenn{x}"
    variables['fenncavabdeyisenler'][fenn_key] = dosya_line[fenncoordinate[x - 1]:fenncoordinate[x]].strip()


def calculate_scores(variables, x, sehvduz, sehvduzsay):
    fenn_key = f"fenn{x}"
    duz_key = f"fenn_{x}_duz"
    sehv_key = f"fenn_{x}_sehv"
    bal_key = f"fenn{x}_bal"
    sual_say = int(variables['fennsualsaydeyisenler'][f"fennsual{x}"])

    for y in range(sual_say):
        student_answer = variables['fenncavabdeyisenler'][fenn_key][y]
        correct_answer = variables['duzguncavabdeyisenler'][f"dzgn_cvb_f{x}"][y]

        if student_answer == correct_answer or correct_answer == '*':
            variables['fennduzdeyisenler'][duz_key] += 1
        elif student_answer != ' ':
            variables['fennsehvdeyisenler'][sehv_key] += 1

    if sehvduz.lower() == 'var':
        variables['fenncembaldeyisenler'][bal_key] = round((variables['fennduzdeyisenler'][duz_key] - (variables['fennsehvdeyisenler'][sehv_key] / int(sehvduzsay))) * float(variables['fennbaldeyisenler'][f"fennbal{x}"]), 2)
    else:
        variables['fenncembaldeyisenler'][bal_key] = round(variables['fennduzdeyisenler'][duz_key] * float(variables['fennbaldeyisenler'][f"fennbal{x}"]), 2)


def main():
    dosya_input_path = get_file_path('OMR scan daxil edin: ')
    dosya_read = read_and_replace(dosya_input_path, replaceletter)
    dosya_list = dosya_read.split("\n") if dosya_read else []

    for i in csvdict.listdict:
        print(i["ad"])
    sinaqformasec = input("Sınaq formasını seçin: ")

    variables, fenncoordinate, sehvduz, sehvduzsay = None, None, None, None
    for i in csvdict.listdict:
        if sinaqformasec == i["ad"]:
            variables, fenncoordinate = initialize_variables(i)
            sehvduz = i["sehvduz"]
            sehvduzsay = i["sehvduzsay"] if sehvduz.lower() == 'var' else None
            break

    if not variables:
        print("Sınaq forması tapılmadı!")
        return

    d.db_first()
    for x in range(1, len(fenncoordinate)):
        d.db_second(x)

    process_student_results(dosya_list, variables, fenncoordinate, sehvduz, sehvduzsay)


if __name__ == "__main__":
    main()
