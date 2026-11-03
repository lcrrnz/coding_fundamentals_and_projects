from pathlib import Path

import FreeSimpleGUI as sg
from pypdf import PdfWriter
from pypdf.errors import PdfReadError


def merge_pdfs(input_paths: list[Path], output_path: Path) -> None:
    writer = PdfWriter()
    try:
        for input_path in input_paths:
            writer.append(str(input_path))

        with output_path.open("wb") as output_file:
            writer.write(output_file)
    finally:
        writer.close()


def main() -> None:
    input_paths: list[Path] = []
    layout = [
        [sg.Text("Select PDF files to combine, in the order listed.")],
        [
            sg.Listbox(
                values=[],
                size=(70, 12),
                key="-FILES-",
                select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED,
                expand_x=True,
                expand_y=True,
            )
        ],
        [
            sg.Button("Add PDFs"),
            sg.Button("Remove Selected"),
            sg.Button("Clear List"),
        ],
        [
            sg.Text("Save merged PDF as:"),
            sg.Input("unidos.pdf", key="-OUTPUT-", expand_x=True),
            sg.Button("Browse..."),
        ],
        [sg.Button("Merge PDFs"), sg.Button("Exit")],
    ]
    window = sg.Window("PDF Merger", layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break

        if event == "Add PDFs":
            selected_files = sg.popup_get_file(
                "Select one or more PDF files",
                multiple_files=True,
                files_delimiter="|",
                file_types=(("PDF files", "*.pdf"),),
            )
            if selected_files:
                for file_path in selected_files.split("|"):
                    path = Path(file_path)
                    if path not in input_paths:
                        input_paths.append(path)
                window["-FILES-"].update(values=[str(path) for path in input_paths])

        elif event == "Remove Selected":
            selected = set(values["-FILES-"] or [])
            input_paths = [path for path in input_paths if str(path) not in selected]
            window["-FILES-"].update(values=[str(path) for path in input_paths])

        elif event == "Clear List":
            input_paths.clear()
            window["-FILES-"].update(values=[])

        elif event == "Browse...":
            output_path = sg.popup_get_file(
                "Choose where to save the merged PDF",
                save_as=True,
                default_path=values["-OUTPUT-"],
                default_extension=".pdf",
                file_types=(("PDF files", "*.pdf"),),
            )
            if output_path:
                window["-OUTPUT-"].update(output_path)

        elif event == "Merge PDFs":
            if not input_paths:
                sg.popup_error("Add at least one PDF file before merging.")
                continue

            output_text = values["-OUTPUT-"].strip()
            if not output_text:
                sg.popup_error("Choose a name and location for the merged PDF.")
                continue

            output_path = Path(output_text)
            if output_path.suffix.lower() != ".pdf":
                sg.popup_error("The output file name must end in .pdf.")
                continue

            if output_path.resolve() in {path.resolve() for path in input_paths}:
                sg.popup_error("The output file cannot be one of the input PDFs.")
                continue

            try:
                merge_pdfs(input_paths, output_path)
            except (OSError, PdfReadError, ValueError) as error:
                sg.popup_error(f"Could not merge the PDF files:\n{error}")
            else:
                sg.popup(f"Merged {len(input_paths)} PDF file(s) into:\n{output_path}")

    window.close()


if __name__ == "__main__":
    main()
