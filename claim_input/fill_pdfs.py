import typing
from PyPDF2 import PdfReader, PdfWriter


def fill_pdf(to_input: dict, filename: str, new_filename: str):
    reader = PdfReader(filename)
    writer = PdfWriter()

    for i in range(0,8):
        page = reader.pages[i]
        writer.add_page(page)

    imp_page = reader.pages[2]
    fields = reader.get_fields()

    for field, text in list(to_input.items())[:-1]:
        print(f"{field}, {text}")
        writer.update_page_form_field_values(
            writer.pages[2], {field: text}
        )
    
    date_field, date = list(to_input.items())[-1]
    writer.update_page_form_field_values(
            writer.pages[4], {date_field: date}
        )

    # write "output" to PyPDF2-output.pdf
    with open(new_filename, "wb") as output_stream:
        writer.write(output_stream)

