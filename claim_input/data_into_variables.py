import typing
from datetime import date

year = "2022"

def get_data_from_text(text: list):
    
    today = date.today()

    extracted_information = {
    "Treatment date": "",
    'Total charge (with currency)': "",
    'Location of claim – Provider’s name and address': "",
    'Location of claim – Provider’s name and address_2': "",
    'Postal/Zip code': "",
    'Description of service' : "MRI", #type
    'Reason for visit': "Memory loss concerns", #type
    'Date signed': today.strftime("%m%d%Y")
}
    for word in text:
        # find date
        if year in word:
            # american notation month then date
            word = word.replace(".", "")
            extracted_information["Treatment date"] = word[2:4] + word[0:2] + year
        
        # find amount 
        elif word == "Betrag":
            next_word = text[text.index(word)+1]
            if next_word.replace(".", "").isnumeric():
                extracted_information["Total charge (with currency)"] = next_word
        
        elif word == "CHF:":
            next_word = text[text.index(word)+1]
            if next_word.replace(".", "").isnumeric():
                extracted_information["Total charge (with currency)"] = next_word

        elif word == "CHF":
            prev_word = text[text.index(word)+1]
            if prev_word.replace(".", "").isnumeric():
                extracted_information["Total charge (with currency)"] = prev_word

        # find doctor name and address
        elif word == "Leistungserbringer" or word == "Rechnungssteller":
            start_index = text.index(word)
            name_address = ""
            i = start_index
            while text[i] != "Zurich" and text[i] != "Zirich" and i < len(text):
                i += 1
                name_address += f" {text[i]}"
            
            extracted_information['Location of claim – Provider’s name and address'] = " ".join(name_address.split()[:-4])
            extracted_information['Location of claim – Provider’s name and address_2'] = " ".join(name_address.split()[-4:-2])
            extracted_information['Postal/Zip code'] = name_address.split()[-2]
        
    return extracted_information

