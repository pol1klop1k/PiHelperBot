import docx

doc = docx.Document("Voprosy_k_ekzamenu_1.docx")

questions = [question.text for question in doc.paragraphs]

