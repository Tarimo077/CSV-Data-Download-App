import PyPDF2
import anvil.server
import os
import anvil.media

@anvil.server.callable
def pdf_gen(pdf):
    # Open the PDF file for reading
    input_pdf_path = "/tmp/input.pdf"
    output_pdf_path = "/tmp/output.pdf"
    
    anvil.media.write_to_file(pdf, input_pdf_path)
    
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        # Create a PDF writer to write the modified content to a new PDF file
        pdf_writer = PyPDF2.PdfFileWriter()

        # Iterate through each page in the PDF
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()  # Extract text from the page
            
            # Search for the specific text you want to find
            if "Receipt #" in text:
                # Add the original page content up to the found text
                pdf_writer.addPage(page)
                
                # Create a new page with additional text
                new_page = PyPDF2.PageObject.createBlankPage(width=page.mediaBox.getWidth(), height=page.mediaBox.getHeight())
                new_page.mergePage(page)
                
                # Add the new text after the found text
                new_text = "My new text is here"
                new_page.mergeTranslatedPage(page, 0, 0, new_text)
                
                pdf_writer.addPage(new_page)
            else:
                pdf_writer.addPage(page)
        
        # Save the modified PDF to the output PDF file
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

    # Return the URL to the saved PDF file
    return anvil.media.from_file(output_file, "application/pdf", '/tmp/output1.pdf')