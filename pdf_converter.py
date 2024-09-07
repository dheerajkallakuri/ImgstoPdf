import os
from fpdf import FPDF
def convert_images_to_pdf(folder_path, output_pdf):
    pdf = FPDF()
    
    images = [img for img in os.listdir(folder_path) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    print(images)
    # images=["img1.png","img2.png"]
    # print(images)

    if images:
        for image in images:
            img_path = os.path.join(folder_path, image)
            pdf.add_page()
            pdf.image(img_path, x=10, y=10, w=190, h=0)
        
        pdf.output(output_pdf, "F")
        print(f"PDF generated successfully: {output_pdf}")
    else:
        print("No images found in the folder for conversion.")