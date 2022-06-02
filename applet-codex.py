
import streamlit as st 
from PIL import Image, ImageOps 
import huggingface as hf
st.set_option('deprecation.showfileUploaderEncoding', False) 
  
def main(): 
    st.title("Photo Editor") 

    image_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

    if image_file is not None: 

        our_image = Image.open(image_file).convert('RGB')

        st.text("Original Image")      ## displaying original photo          ##                              # in the app           ##       images uploaded by the user

        ## generate me a stremalit applet that inpaints the image with a click of a button!
        try :
            st.button("Inpaint")
            our_image = ImageOps.invert(our_image)
            st.image(our_image)
        except :
            st.text("No image selected")

            ## now make another button that says 'RIP' when clicking rip have it download the image you selected
            try :
                st.button("RIP")
                st.image(our_image)
            except :
                st.text("No image selected")

                ## now make a gui
                ## make a slider that changes the brightness of the image  

try :
    main()
except :
    st.text("No image selected")


    ## now make a inpainting editor gui that asks for a color wheel 
    try :
        st.button("Inpaint")
        our_image = ImageOps.invert(our_image)
        st.image(our_image)
    except :
        st.text("No image selected")

        ## now make another button that says 'RIP' when clicking rip have it download the image you selected
        try :
            st.button("RIP")
            st.image(our_image)
        except :
            st.text("No image selected")

            ## now make a gui
            ## make a slider that changes the brightness of the image
            ## make a gui that manages the photo editor
            ## and can edit the photo with a text prompt using stylegan on huggingface
 ## make a text prompt that per

                ## now make another button that says 'RIP' when clicking rip have it download the image you selected
  
                    ## now make a gui
                    ## make a slider that changes the brightness of the image
                    ## make a gui that manages the photo editor
                    ## and can edit the photo with a text prompt using stylegan on huggingface
                   
                    ## make a text prompt that per

                            ## now make a gui
                            ## make a slider that changes the brightness of the image
                            ## make a gui that manages the photo editor
                            ## and can edit the photo with a text prompt using stylegan on huggingface
                              