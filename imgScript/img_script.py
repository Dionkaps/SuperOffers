import os
import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from PIL import Image
from io import BytesIO

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image = image.convert('RGB')  #Convert the image to RGB format
        image_filename = f"{filename}.png"
        image.save(image_filename, format='PNG')
        print(f"Image '{image_filename}' downloaded and saved as PNG successfully.")
    else:
        print(f"Failed to download image from URL: {url}")

def save_product_images(product_data):
    for product in product_data:
        product_name = product['name']
        id = product['id']
        search_query = product_name.replace(" ", "+")
        search_url = f"https://www.google.com/search?q={search_query}&tbm=isch"

        response = requests.get(search_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            image_elements = soup.find_all('img')

            for img in image_elements:
                image_url = img['src']
                if image_url.startswith('http'):
                    parsed_url = urlparse(image_url)
                    image_filename = f"{id}"
                    download_image(image_url, image_filename)
                    break

def main():
    json_data = '''
[
     {
      "id": "0",
      "name": "Χρυσά Αυγά Εξαίρετα Φρέσκα Large 6τ Χ 63γρ Πλαστ Θήκη",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d2babbc7355444ca0d27633207e4743"
    },
    {
      "id": "2",
      "name": "Κριθαράκι Μίσκο Χονδρό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "3",
      "name": "Proderm Ενυδατική Κρέμα 150ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "4",
      "name": "Γιώτης Κρέμα Παιδικη Φαρίν Λακτέ Μπισκότο 300γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "5",
      "name": "Δωδώνη Γιαούρτι Στραγγιστό 2% 1Kg",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "6",
      "name": "Καραμολέγκος Παξαμάς Σικαλης 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "7",
      "name": "Neomat Σκόνη Πλυντηρίου Ρούχων Άγριο Τριαντάφυλλο 45μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "8",
      "name": "Ariel Υγρό Απορρυπαντικό Ρούχων Alpine 28μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "9",
      "name": "Fairy Υγρό Απορρυπαντικό Πιάτων Power Spray 375ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "10",
      "name": "Λαυράκια Υδατ  Ελλην 400/600 Μεσογ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "11",
      "name": "Μήλα Στάρκιν Ζαγορ Πηλίου ΠΟΠ Κατ Έξτρα",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "12",
      "name": "Πορτοκ Βαλέντσια Εγ Χυμ Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "13",
      "name": "Μπούτι Χοιρινό Α/Ο Νωπό Ελλ Χ/Δ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "14",
      "name": "Αγγουράκια Κιλ Τυπ Νειλ – Τυπ Κνωσ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "15",
      "name": "Κοτοπουλα Ολοκληρα Νωπα Χυμα Τ.65% Π.Α.Ελλην",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "16",
      "name": "Κολοκυθάκια Εγχ Με Ανθό",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "17",
      "name": "Μελιτζάνες Φλάσκες Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "18",
      "name": "Μελιτζάνες Φλάσκες Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "19",
      "name": "Λάπα Βόειου Α/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "20",
      "name": "Μπρόκολα Πράσινα Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "23",
      "name": "Καρπούζια Μίνι Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "24",
      "name": "Σπάλα Βόειου/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "25",
      "name": "Λαιμός Χοιρινός Μ/Ο Νωπός Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "26",
      "name": "Τσίπουρα Υδατ  Καθαρ Ελλην G 400/600 Μεσογ Συσκ/Νη",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "28",
      "name": "Κιλότο Βόειου Α/Ο Νωπό Ελλ Εκτρ Άνω Των 5 Μην",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "29",
      "name": "Μπανάνες Dole Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "30",
      "name": "Μήλα Στάρκιν Ψιλά Συσκ/Να ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "31",
      "name": "Ελιά Νεαρού Μοσχ Α/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "32",
      "name": "Πορτοκ Μερλίν - Λανε Λειτ- Ναβελ Λειτ Εγχ Χυμ Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "33",
      "name": "Κατσίκια Νωπά Ελλην Γαλ Ολοκλ Χ/Κ Χ/Σ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d3385ff161f0423aa364017d4413fa77"
    },
    {
      "id": "34",
      "name": "Μήλα Στάρκιν Χύμα",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "35",
      "name": "Μπούτι Χοιρινό Α/Ο Νωπό Εισ Χ/Δ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "36",
      "name": "Σαρδέλλες Νωπές Ελλην Μεσογ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c487e038079e407fb1a356599c2aec3e"
    },
    {
      "id": "38",
      "name": "Ελιά Βόειου Α/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "39",
      "name": "Ελιά Βόειου Α/Ο Νωπή Ελλ Εκτρ Άνω Των 5 Μην ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "41",
      "name": "Πατάτες  Ελλ Κατ Α Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "42",
      "name": "Μήλα Φουτζι Εγχ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "43",
      "name": "Λαυράκια Υδατ  Καθαρ Ελλην400/600 Μεσογ Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "44",
      "name": "Μπριζόλες Καρέ/Κόντρα Χοιρ Νωπές Ελλ Μ/Ο ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "45",
      "name": "Γαύρος Νωπός Ελλην Μεσόγ Ολόκλ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c487e038079e407fb1a356599c2aec3e"
    },
    {
      "id": "46",
      "name": "Τοματίνια Βελανίδι Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "47",
      "name": "Μπριζόλες Καρέ/Κόντρα Χοιρ Νωπές Εισ Μ/Ο ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "48",
      "name": "Μπανάνες Υπολ Μάρκες ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "49",
      "name": "Μπρόκολα Πράσινα Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "50",
      "name": "Πατάτες  Κύπρου  Κατ Α Συσκ/Νες",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "51",
      "name": "Κρεμμύδια Κόκκινα Ξερά Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "52",
      "name": "Ντομάτες Τσαμπί Υδροπ Εγχ  Α",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "53",
      "name": "Ροδάκινα Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "54",
      "name": "Λαιμός Χοιρινός Μ/Ο Νωπός Ελλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "55",
      "name": "Νεκταρίνια Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "56",
      "name": "Καρπούζια Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "57",
      "name": "Κολοκυθάκια Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "58",
      "name": "Σολομός Νωπός Φιλετ/νος Με Δέρμα Υδ Νορβ/Εισαγ  Β.Α Ατλ Συσκ/νος",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "59",
      "name": "Ντομάτες Εισ Α",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "60",
      "name": "Ντομάτες Εγχ Υδροπ Α ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "62",
      "name": "Τσίπουρα Υδατ Ελλην G 400/600 Μεσογ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "63",
      "name": "Κιλότο Νεαρού Μοσχ Α/Ο Νωπό Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "64",
      "name": "Πορτοκάλια Βαλέντσια Εισ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "65",
      "name": "Κιλότο Βόειου Α/Ο Νωπό Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "66",
      "name": "Λεμόνια Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "67",
      "name": "Μπανάνες Chiquita Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "68",
      "name": "Κοτόπουλα Νωπά Ολόκλ Τ.65% Μιμίκος  Π.Α.Ελλην Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "70",
      "name": "Πορτοκ Μερλίν - Λανε Λειτ- Ναβελ Λειτ Κατ Α Εγχ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "71",
      "name": "Στήθος Φιλέτο Κοτ Ελλην. Νωπό Συσκ/Νο",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "72",
      "name": "Κρεμμύδια Κόκκινα Ξερά Εισ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "73",
      "name": "Πορτοκ Βαλέντσια  Κατ Α Εγχ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "77",
      "name": "Στήθος Φιλέτο Κοτ Ελλην. Νωπό Ε/Ζ Χύμα ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "78",
      "name": "Αρνιά Νωπά Ελλην Γαλ Ολοκλ Χ/Κ Χ/Σ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0936072fcb3947f3baf83e31bb5c1cab"
    },
    {
      "id": "79",
      "name": "Αγγούρια Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "80",
      "name": "Σπάλα Νεαρού Μοσχ Α/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "81",
      "name": "Σπάλα Βόειου Α/Ο Νωπή Ελλ Εκτρ Άνω Των 5 Μην",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "82",
      "name": "Quanto Μαλακτικό Ρούχων Ελληνικά Νησιά 18μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "85",
      "name": "Misko Παραδ Χυλοπίτες Με Αυγά Μετσόβου 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "87",
      "name": "Βλάχας Γάλα Εβαπορέ Ελαφρύ 410γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "88",
      "name": "Κοτόπουλα Νωπά Ολόκλ Τ.65% Π.Α.Ελλην Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "89",
      "name": "Ferrero Kinder Delice Κέικ 39γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "90",
      "name": "7 Days Bake Rolls Pizza 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47b5f0016f4f0eb79e3a4b932f7577"
    },
    {
      "id": "91",
      "name": "Nan Optipro 4 Γάλα Σε Σκόνη Δεύτερης Βρεφικής Ηλικίας 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "93",
      "name": "Κρίς Κρίς Τόστιμο Ψωμί Τόστ Ολικής Άλεσης 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "94",
      "name": "Καραμολέγκος Ψωμί Τόστ Δέκα Χωριάτικο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "95",
      "name": "Babylino Πάνες Μωρού Sensitive 9-20 κιλ Nο 4+ 19τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "96",
      "name": "Κορπή Φυσικό Μεταλλικό Νερό 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "98",
      "name": "Άλτις Κλασσικό Ελαιόλαδο 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "99",
      "name": "Maggi Μείγμα Λαχανικών Νοστιμιά Σε Σκόνη 130γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "100",
      "name": "Pampers Πάνες Premium Care Nο 3 5-9 κιλ 20τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "101",
      "name": "Johnson Baby Βρεφικό Σαμπουάν Αντλιά 300ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "102",
      "name": "Μάκβελ Μακαρόνια Σπαγγέτι Ν6 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "103",
      "name": "Ω3 Αυγά Αμερικ Γεωργ Σχολής 6τ Large 63-73γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d2babbc7355444ca0d27633207e4743"
    },
    {
      "id": "104",
      "name": "Κρι Κρι Γιαούρτι Στραγγιστό 2% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "106",
      "name": "Παπαδοπούλου Τριμμα Φρυγανιας Τριμμα 180γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "107",
      "name": "3 Άλφα Ρεβύθια Χονδρά Εισαγωγής 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "108",
      "name": "Γιώτης Αλεύρι Φαρίνα Ολικής Άλεσης 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "109",
      "name": "Λεμόνια Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "111",
      "name": "Καρότα Εγχ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "112",
      "name": "Κοκκινόψαρο  Κτψ Εισ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "113",
      "name": "Τοπ Κρέμα Βαλσάμικο Με Λεμόνι & Μέλι 200ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "115",
      "name": "Νουνού Κρέμα Γάλακτος Πλήρης 330ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4e4cf5616e0f43aaa985c1300dc7109e"
    },
    {
      "id": "117",
      "name": "Dettol Spray Γενικού Καθαρισμού Υγιεινή Και Ασφάλεια Λεμόνι Μέντα 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "118",
      "name": "Agrino Φασόλια Γίγαντες Ελέφαντες Καστοριάς Π.Γ.Ε. 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "120",
      "name": "Nestle Φαρίν Λακτέ 350γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "121",
      "name": "Barilla Maccheroncini Μακαρόνια Για Παστίτσιο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "122",
      "name": "Χρυσά Αυγά Ελληνικά Βιολ 6τ Medium 348γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d2babbc7355444ca0d27633207e4743"
    },
    {
      "id": "123",
      "name": "Barilla Ζυμαρικά Capellini No1 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "125",
      "name": "Zewa Χαρτί Υγείας Deluxe Χαμομήλι 3 Φύλλα 8τεμ 768γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "126",
      "name": "Elite Φρυγανιές Ολικής Άλεσης 180γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "127",
      "name": "Agrino Φακές Ψιλές Εισαγωγής 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "128",
      "name": "Δέλτα Γάλα 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "129",
      "name": "Twix Σοκολάτα Μπισκότο 50γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "130",
      "name": "Misko Μακαρόνια Σπαγγέτι Ν3 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "132",
      "name": "Υφαντής Γαλοπούλα Καπνιστή 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "133",
      "name": "Μινέρβα Χωριό Μαργαρίνη Με Ελαιόλαδο 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "134",
      "name": "Γιώτης Ανθός Ορύζης 150γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "135",
      "name": "Libresse Σερβιέτες Ultra Thin Long Wings 8τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "136",
      "name": "Viakal Υγρό Καθαρισμού Κατά Των Αλάτων 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "137",
      "name": "Γιώτης Κρέμα Παιδική Φαρίν Λακτέ 300γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "138",
      "name": "Pampers Πάνες Premium Care Nο 4 8-14 κιλ 52τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "139",
      "name": "Nestle Fitness Μπαρες Δημητριακών Crunchy Caramel 6X23.5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "141",
      "name": "Dettol Κρεμοσάπουνο 250ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "142",
      "name": "Ωμέγα Special Ρύζι Νυχάκι 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "143",
      "name": "Johnson Βρέφικη Πουδρα Σωματος 200γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "144",
      "name": "Johnson Baby Βρεφικό Σαμπουάν Χαμομήλι Αντλιά 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "145",
      "name": "Babylino Sensitive No4+ Econ 9-20κιλ 46τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "146",
      "name": "Κανάκι Pizza Special 3 Χ 460γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3f38edda7854447a837956d64a2530fa"
    },
    {
      "id": "148",
      "name": "Septona Σαμπουάν Και Αφρόλουτρο Βρεφικό Με Λεβαντα 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "149",
      "name": "Crunch Σοκολάτα Γάλακτος 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "150",
      "name": "3 Άλφα Ρύζι Γλασσέ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "151",
      "name": "Knorr Κύβοι Ζωμού Κότας 6λιτ 12τεμάχια",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "153",
      "name": "Babylino Πάνες Μωρού Sensitive 16+ κιλ No 6 15τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "154",
      "name": "3 Άλφα Ρύζι Γλασέ 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "155",
      "name": "Knorr Κύβοι Ζωμού Λαχανικών 12λιτ 24τεμάχια",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "156",
      "name": "Νίκας Σαλαμι Αέρος Συκευασμενο 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "157",
      "name": "Overlay Ultra Spray Λιποκαθαριστής Λεμόνι 650ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "160",
      "name": "Άριστον Αλάτι Ιμαλαΐων Φιάλη 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "161",
      "name": "Στεργίου Κρουασάν Βιέννης Με Κρέμα Σοκολάτα 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "163",
      "name": "3 Άλφα Ρύζι Νυχάκι Ελληνικό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "165",
      "name": "Neomat Υγρό Απορρυπαντικό Ρούχων Τριαντάφυλλο 62μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "166",
      "name": "Knorr Κύβοι Ζωμού Λαχανικών Extra Γεύση 147γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "168",
      "name": "Μύλοι Αγίου Γεωργίου Αλεύρι Για Πίτσα 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "169",
      "name": "Παπαδημητρίου Balsamico Με Μέλι 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "170",
      "name": "Χρυσή Ζύμη Κρουασάν Βουτύρου 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "171",
      "name": "Dr Beckmann Καθαριστικο Φουρνου 375ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "172",
      "name": "Fouantre Γαλοπούλα Σε Φέτες 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "173",
      "name": "Ava Υγρό Πιάτων Perle Χαμομήλι/Λεμόνι 1500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "174",
      "name": "Κανάκι Βάση Πίτσας Κατεψυγμένη 660γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "175",
      "name": "Νίκας Μπέικον Καπνιστό Συσκευασμένο 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "176",
      "name": "Knorr Ζωμός Κότας Σε Κόκκους Extra Γεύση 88γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "177",
      "name": "Ίον Σοκολάτα Γάλακτος 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "178",
      "name": "Alfa Τριγωνάρια Με Τυρί Ανεβατο Κατεψυγμένα 750γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "179",
      "name": "Libresse Σερβιέτες Invisible Normal 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "180",
      "name": "Johnson Baby Βρεφικό Σαμπουάν Χαμομήλι 300ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "181",
      "name": "Agrino Ρύζι Σουπέ Γλασέ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "182",
      "name": "Καραμολέγκος Δέκα Αρτοσκεύασμα Σταρένιο Σε Φέτες 550γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "184",
      "name": "Μετέωρα Ξύδι Λευκού Κρασιού 400ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "185",
      "name": "Babylino Πάνες Μωρού Sensitive 4 - 9 κιλ No 3 22τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "186",
      "name": "Zewa Χαρτι Κουζίνας Wisch And Weg Economy 3τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "187",
      "name": "Γιώτης Φρουτόκρεμα 5 Φρούτα 300γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "189",
      "name": "Κατσέλης Κριτσίνια Μακεδονικά 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "190",
      "name": "Βλάχας Γάλα Εβαπορέ Πλήρες 410γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "191",
      "name": "Παπαδοπούλου Παξιμαδάκια Σίτου 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "192",
      "name": "Ajax Υγρό Κατά Των Αλάτων Spray Expert 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "193",
      "name": "Ωμέγα Special Ρύζι Basmati 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "194",
      "name": "Κοντοβερός Σολωμός Φιλέτο Chum 595γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "196",
      "name": "Γιώτης Sanilac 2 Γάλα Σε Σκόνη Δεύτερης Βρεφικής Ηλικίας 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "197",
      "name": "Δωδώνη Γιαούρτι Στραγγιστό 8% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "199",
      "name": "Pampers Πάνες Μωρού Premium Care Newborn 2-5κιλ 26τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "200",
      "name": "Agrino Ρύζι Φανσύ Για Γεμιστά Χ Γλουτ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "201",
      "name": "Dettol Κρεμοσάπουνο Soothe 250ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "202",
      "name": "Babylino Sensitive No6 Econ 15-30κιλ 40τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "203",
      "name": "Anatoli Πιπέρι Μαύρο Μύλος 45gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "204",
      "name": "Melissa Σιμιγδάλι Ψιλό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "205",
      "name": "Εν Ελλάδι Μπέικον Καπνιστό Σε Φέτες 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "206",
      "name": "Εύρηκα Bright Ενισχυτικό Πλύσης Πολυκαθαριστικό Λεκέδων 500g",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "207",
      "name": "Μινέρβα Αραβοσιτέλαιο 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "208",
      "name": "Μακβελ Μακαρόνια Σπαγγέτι No 10 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "209",
      "name": "Dettol Υγρό Πολυκαθαριστικό Αντιβακτηριδιακό 500ml Sparkling Lemon & Lime Burst Power & Fresh",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "210",
      "name": "Vanish Oxi Action Ενισχυτικό Πλεύσης 1γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "211",
      "name": "Nan Optipro 1 Γάλα Σε Σκόνη Πρώτης Βρεφικής Ηλικίας 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "212",
      "name": "Kit Kat Σοκολάτα 41,5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "213",
      "name": "Alfa Λουκανικοπιτάκια Κουρού 800gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "214",
      "name": "Ajax Άσπρος Σίφουνας Λεμόνι 1000ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "216",
      "name": "Μέλισσα Μακαρόνια Σπαγγετίνη Νο 10 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "217",
      "name": "Ήρα Αλάτι Μαγειρικό 1kg",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "218",
      "name": "Elite Φρυγανιές Σίκαλης 180γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "219",
      "name": "Kellogg’s Δημητριακά Corn Flakes 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "220",
      "name": "3 Άλφα Φασόλια Γίγαντες Εισαγωγής 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "221",
      "name": "Agrino Ρύζι Φάνσυ Ελλάδας 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "222",
      "name": "Libero Swimpants Πάνες Midi 10-16κιλ 6τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "223",
      "name": "Pampers Πάνες Μωρού 31τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "225",
      "name": "Γιώτης Sanilac 1 Γάλα Σε Σκόνη Πρώτης Βρεφικής Ηλικίας 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "226",
      "name": "Αλλατίνη Κέικ Κακάο Με Κομμάτια Σοκολάτας 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "227",
      "name": "Παπαδοπούλου Αρτοσκεύασμα Πολύσπορο 540γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "228",
      "name": "Ava Υγρό Πιάτων Action Λευκο Ξυδι Αντλια 650ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "229",
      "name": "Χρυσά Αυγά Φρέσκα Medium 53/63 γρ.τεμ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d2babbc7355444ca0d27633207e4743"
    },
    {
      "id": "231",
      "name": "Kellogg's Δημητριακά Choco Pops Chocos 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "232",
      "name": "Αύρα Φυσικό Μεταλλικό Νερό 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "233",
      "name": "Almiron-2 Γάλα Σε Σκόνη Δεύτερης Βρεφικής Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "235",
      "name": "Κανάκι Tυροπιτάκια Κουρού 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "236",
      "name": "Παν Κρέμα Βαλσάμικο 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "237",
      "name": "Κατσέλης Κριτσίνια Μακεδονικά Ολικής Άλεσης 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "238",
      "name": "Misko Μακαρόνια Για Παστίτσιο Ν2 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "239",
      "name": "Μάννα Παξιμάδια Κριθαρένιο 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "240",
      "name": "Misko Ολικής Άλεσης Μακαρόνια Σπαγγέτι Ν6 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "241",
      "name": "Dixan Υγρό Απορρυπαντικό Ρούχων Άνοιξης 30μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "242",
      "name": "Iglo Κροκέτες Ψαριών Κατεψυγμένες 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "243",
      "name": "Pampers Πάνες Premium Care Nο 3 5-9 κιλ 60τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "244",
      "name": "Pampers Πάνες Premium Care Νο 2 4-8κιλ 23τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "245",
      "name": "Γιώτης Αλεύρι Φαρίνα Πορτοκαλί 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "246",
      "name": "Pescanova Μπακαλιάρος Ρολό Φιλeto 480γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "247",
      "name": "Νουνού Κρέμα Γάλακτος Light 200ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4e4cf5616e0f43aaa985c1300dc7109e"
    },
    {
      "id": "248",
      "name": "Misko Μακαρόνια Σπαγγέτι Ν5 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "249",
      "name": "Dirollo Τυρί Ημισκλ 14% Λιπ Φετ 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "250",
      "name": "Χρυσή Ζύμη Λουκανικοπιτάκια Κατεψυγμένα Κουρού 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "251",
      "name": "Septona Παιδικό Αφρόλουτρο & Σαμπουάν Αγορια 750ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "252",
      "name": "Ava Υγρό Πιάτων Perle Σύμπλεγμα Βιταμινών 430ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "253",
      "name": "Neslac Επιδόρπιο Γάλακτος Μπισκότο 4Χ100γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "254",
      "name": "Μάσκα προσώπου 10τεμ 1 χρήση",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "255",
      "name": "Septona Σαμπουάν Και Αφρόλουτρο Βρεφικό Με Αλοη 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "256",
      "name": "Υφαντής Γαλοπούλα Βραστή 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "257",
      "name": "Baby Care Μωρομάντηλα Χαμομήλι Minipack 12τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "92680b33561c4a7e94b7e7a96b5bb153"
    },
    {
      "id": "258",
      "name": "Άλτις Ελαιόλαδο Δοχείο 4λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "259",
      "name": "Υφαντής Παριζακι Γαλοπούλας 330γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "260",
      "name": "Kleenex Χαρτί Υγείας 2 Φύλλα 12τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "261",
      "name": "Pampers Πάνες Μωρού Premium Care Nο 6 13+κιλ 38τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "262",
      "name": "Χρυσή Ζύμη Χωριάτικο Φυλλο Κατεψυγμένο 700γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "263",
      "name": "7 Days Κρουασάν Κακάο 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "264",
      "name": "Χρυσή Ζύμη Μπουγάτσα Θεσσαλονίκης Με Πραλίνα 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "265",
      "name": "Μέλισσα Κριθαράκι Χονδρό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "267",
      "name": "Cajoline Συμπυκνωμένο Μαλακτικό Blue Fresh 30μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "269",
      "name": "Calgon Αποσκληρυντικό Νερού Πλυντηρίου Ρουχων Gel 1.5λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "271",
      "name": "7 Days Swiss Roll Κακάο 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "272",
      "name": "Αλλατίνη Κέικ Βανίλια Με Κακάο 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "273",
      "name": "Μινέρβα Χωριό Ορεινές Περιοχές Ελαιόλαδο Παρθένο 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "274",
      "name": "Υφαντής Παριζάκι 330γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "275",
      "name": "Μέλισσα Κριθαράκι Μέτριο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "276",
      "name": "Παπαδημητρίου Balsamico Βιολογικό Καλαμάτας 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "277",
      "name": "Ajax Υγρό Γενικού Καθαρισμού Kloron Lila 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "279",
      "name": "Παπαδοπούλου Κριτσίνια Σουσάμι 130γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "280",
      "name": "Αλλατίνη Φαρίνα Κέικ Φλάουρ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "281",
      "name": "Kellogg's Special K Μπάρα Δημητριακών Με Ξηρούς Καρπούς Καρύδα Και Κασioυς 4Χ28γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "282",
      "name": "Άλτις Παραδοσιακό Ελαιόλαδο Παρθένο 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "283",
      "name": "Κορπή Φυσικό Μεταλλικό Νερό1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "284",
      "name": "Maggi Κύβοι Ζωμού Λαχανικών 6λιτ 12τεμ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "285",
      "name": "Βίκος Φυσικό Μεταλλικό Νερό 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "287",
      "name": "Κρι Κρι Σπιτικό Επιδόρπιο Γιαουρτιού 5% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "288",
      "name": "Κρίς Κρίς Ψωμί Τόστ Μπρίος 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "290",
      "name": "Skip Υγρό Απορρυπαντικό Ρούχων Spring Fresh 42μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "291",
      "name": "Κανάκι Ζύμη Κατεψυγμένη Κουρού 700γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "292",
      "name": "Κιχί Πίτα Με Πράσο Ταψί Κατεψυγμένο 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "293",
      "name": "Ίον Σοκολάτα Γάλακτος Αμυγδάλου 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "294",
      "name": "Alfa Μπουγάτσα Με Σπανάκι Και Τυρί Κατεψυγμένη 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "296",
      "name": "Pampers Πάνες Μωρού Premium Pants Nο 4 9-15κιλ 38τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "297",
      "name": "Zewa Deluxe Χαρτί Υγείας 3 Φύλλα 8τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "298",
      "name": "Almiron-1 Γάλα Σε Σκόνη Πρώτης Βρεφικής Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "299",
      "name": "Στεργίου Κέικ Ανάμικτο 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "300",
      "name": "Lacta Σοκολάτα Γάλακτος 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "301",
      "name": "Softex Χαρτί Υγείας Super Giga 2 Φύλλα 12τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "303",
      "name": "Dettol Υγρό Καθαριστικό Αντιβακτηριδιακό Κουζινας 500ml Με Ενεργο Οξυγονο Power & Pure",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "304",
      "name": "Μέλισσα Σπαγγέτι Ολικής Άλεσης 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "305",
      "name": "Παπαδημητρίου Κρέμα Balsamico Με Ρόδι Με Στέβια 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "306",
      "name": "Nan Optipro 2 Γάλα Σε Σκόνη Δεύτερης Βρεφικής Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "307",
      "name": "Uncle Bens Ρύζι Basmati 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "308",
      "name": "Baby Care Μωρόμαντηλα Sensitive 63τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "92680b33561c4a7e94b7e7a96b5bb153"
    },
    {
      "id": "310",
      "name": "Barilla Cannelloni 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "311",
      "name": "Klinex Υγρό Καθαρισμού Μπάνιου Spray 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "314",
      "name": "Ajax Uλιτra Υγρό Γενικού Καθαρισμού Λεμόνι 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "315",
      "name": "Agrino Ρύζι Λαΐς Καρολίνα 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "316",
      "name": "Maggi Barilla Spaghettoni No7 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "317",
      "name": "Pampers Premium Care No 5 11-18κιλ 44τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "318",
      "name": "CIF Spray Κουζίνας 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "319",
      "name": "Εύρηκα Υγρό Απορρυπαντικό Ρούχων Μασσαλίας 30μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "320",
      "name": "Κανάκι Λουκανικοπιτάκια Κατεψυγμένα 920γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "321",
      "name": "Nan Optipro Γάλα Τρίτης Βρεφικής Ηλικίας 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "323",
      "name": "Παπαδοπούλου Φρυγανιές Χωριάτικες Ολικής Άλεσης 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "324",
      "name": "Alfa Κασερόπιτα Πηλίου Κατεψυγμένη 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "325",
      "name": "Molto Κρουασάν Πραλίνα 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "326",
      "name": "3 Αλφα Ρύζι Καρολίνα 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "327",
      "name": "Folie Κρουασάν Κρέμα Κακαο 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "328",
      "name": "7 Days Παξιμαδάκια Mini Κλασική Γεύση Bake Rolls 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "329",
      "name": "Bref Wc Power Active Αρωματικό Τουαλέτας Πεύκο 50γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "330",
      "name": "Johnson Baby Βρεφικό Σαμπουάν Αντλιά 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "331",
      "name": "Μύλοι Αγίου Γεωργίου Καλαμποκάλευρο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "332",
      "name": "Akis Καλαμποκάλευρο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "333",
      "name": "Όλυμπος Γιαούρτι Στραγγιστό 10% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "334",
      "name": "Κρι Κρι Σπιτικό Επιδόρπιο Γιαουρτιού 2% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "335",
      "name": "Adoro Κρέμα Γάλακτος 35% Λιπαρά 200ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4e4cf5616e0f43aaa985c1300dc7109e"
    },
    {
      "id": "336",
      "name": "Τράτα Τόνος Φιλέτο 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "337",
      "name": "Snickers Σοκολάτα 50γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "338",
      "name": "Nutricia Biskotti Ζωάκια 180γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "339",
      "name": "Septona Σερβιέτες Sensitive Ultra Plus Night 8τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "340",
      "name": "Neslac Επιδόρπιο Γάλακτος Βανίλια 4Χ100γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "341",
      "name": "Κρίς Κρίς Τόστιμο Ψωμί Τόστ Σταρένιο 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "342",
      "name": "Maggi Κύβοι Ζωμού Κότας 6λιτ 12τεμ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "343",
      "name": "Στεργίου Κρουασάνάκια Με Γέμιση Πραλίνα 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "344",
      "name": "Skip Σκόνη Spring Fresh 45μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "345",
      "name": "Klinex Καθαριστικό Τουαλέτας Block Ροζ Μανόλια 55γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "346",
      "name": "Agrino Φασόλια Μέτρια 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "347",
      "name": "Nestle Φρουτοπουρές 4 Φρούτα 90γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "348",
      "name": "Νίκας Ωμοπλάτη Χωρίς Γλουτένη 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "349",
      "name": "Babylino Πάνες Μωρού Sensitive No 5+ Εως 27 κιλ 16τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "350",
      "name": "Softex Χαρτοπετσέτες Λευκές 30x30 56τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "351",
      "name": "Φάγε Total Γιαούρτι Στραγγιστό 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "352",
      "name": "Κεραμάρη Μάννα Αλεύρι Για Πίτες 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "355",
      "name": "Babylino Πάνες Μωρού Sensitive Nο7 17+ κιλ 14τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "356",
      "name": "Παπαδημητρίου Κρέμα Balsamico Λευκή 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "357",
      "name": "3 Άλφα Ρύζι Νυχάκι 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "358",
      "name": "7 Days Κρουασάν Mini Κακάο 107γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "359",
      "name": "Roli Καθαριστικό Σκόνη Για Όλες Τις Επιφάνειες Λεμονί 500γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "360",
      "name": "Pampers Πάνες Μωρού Premium Pants Nο 5 12-17κιλ 34τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "361",
      "name": "Γιώτης Μπισκοτόκρεμα 300γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "362",
      "name": "Creta Farm Λουκάνικα Τρικάλων Με Πράσο 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "364",
      "name": "Uncle Bens Ρύζι 10 λεπτά 4Χ125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "365",
      "name": "Τράτα Σαρδέλες Φιλέτο Κατεψυγμένες 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "366",
      "name": "Alfa Πίτσα Μαργαρίτα Κατεψυγμένη 730γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3f38edda7854447a837956d64a2530fa"
    },
    {
      "id": "367",
      "name": "Libero Swimpants Πάνες Small 7-12κιλ 6τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "368",
      "name": "Αύρα Φυσικό Μεταλλικό Νερό 1.5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "370",
      "name": "3 Άλφα Φασόλια Χονδρά Εισαγωγής 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "371",
      "name": "Νίκας Γαλοπούλα Καπνιστή Φέτες 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "372",
      "name": "Babylino Πάνες Μωρού Sensitive 3-6κιλ Nο 2 26τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "373",
      "name": "Duck Στερεό Block Aqua Blue 40ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "374",
      "name": "Almiron-3 Γάλα Σε Σκόνη Τρίτης Βρεφικής Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "375",
      "name": "Klinex Advance Απορρυπαντικό Ρούχων Πλυντηρίου Με Χλώριο 2λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "376",
      "name": "Παπαδοπούλου Ψωμί Τόστ Plus Σίτου 700γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "377",
      "name": "Nan Optipro Γάλα Τρίτης Βρεφικής Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "378",
      "name": "Soupline Συμπυκνωμένο Μαλακτικό Ρούχων Λεβάντα 28μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "379",
      "name": "Babylino Πάνες Μωρού Sensitive 11 - 25κιλ No 5 18τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "380",
      "name": "Nesquik Δημητριακά Extra Choco Waves 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "381",
      "name": "Babylino Sensitive Econ Ν5+ 13-27κιλ 42τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "382",
      "name": "Ζαγόρι Φυσικό Μεταλλικό Νερό 1.5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "383",
      "name": "Υφαντής Hot Dog Nuggets Κοτόπουλου 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "384",
      "name": "Septona Παιδικό Σαμπουάν Κορίτσια 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "386",
      "name": "Γιώτης Mείγμα Παγωτού Καιμάκι 508γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "390",
      "name": "Ντομάτες Εγχ Υπαιθρ Α ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "392",
      "name": "Πέρκα Φιλέτο Κτψ Εισ Ε/Ζ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "394",
      "name": "Ντομάτες Εγχ Υπαιθρ Β ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "395",
      "name": "Johnson's Baby Κρέμα Μαλλ Χωρ Κομπ 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "398",
      "name": "Δέλτα Γάλα Πλήρες 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "399",
      "name": "Δέλτα Γάλα Πλήρες 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "400",
      "name": "Δέλτα Γάλα Ελαφρύ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "401",
      "name": "Δέλτα Milko Γάλα Παστερ 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "402",
      "name": "Δέλτα Milko Κακάο 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "403",
      "name": "Δέλτα Ρόφημα Advance Υψ Παστ Μπουκ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "404",
      "name": "Δέλτα Ρόφημα Advance 80% Λιγ Λακτ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "405",
      "name": "Δέλτα Mmmilk Γάλα Οικογεν Χαρτ 1,5% 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "406",
      "name": "Δέλτα Γάλα Daily Υψ Παστ Χ Λακτ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "407",
      "name": "Δέλτα Milko Κακάο 450ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "408",
      "name": "Μεβγάλ Γάλα Αγελ Λευκό Light 1,5% 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "409",
      "name": "Μεβγάλ Γάλα Αγελ Λευκό Πλήρες 3,5% 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "411",
      "name": "Μεβγάλ Topino Απαχο Γάλα Κακάο 450ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "412",
      "name": "Όλυμπος Γάλα Ζωής Λευκό Ελαφρύ Παστ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "413",
      "name": "Όλυμπος Γάλα Επιλεγμ 3,7% Λ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "414",
      "name": "Όλυμπος Γάλα Επιλεγμ 1,5% Λ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "415",
      "name": "Όλυμπος Γάλα Βιολ Υψηλ Παστ 3,7% Λ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "416",
      "name": "Όλυμπος Γάλα Freelact 1λιτ Χ.Λακτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "417",
      "name": "Εβόλ Γάλα Παστερ Κατσικ Βιολ 590ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "418",
      "name": "Εβόλ Γιαούρτι Κατσικίσιο Βιολ 190γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "419",
      "name": "Εβόλ Γάλα Παστερ Διαλεχτο 3,7% Λ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "420",
      "name": "Νουνού Ρόφημα Γάλακτος Calciplus 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "422",
      "name": "La Vache Qui Rit Τυροβουτιές 4Χ35γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "423",
      "name": "Moscato D'Αsti Casarito Κρασί 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "424",
      "name": "Joya Ρόφημα Σογιας Bio Χ Ζαχ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "425",
      "name": "Calliga Demi Sec Ροζέ Οίνος 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "429",
      "name": "Λακώνια Χυμός Νέκταρ Πορ/Μηλ/Βερ 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "433",
      "name": "Κανάκι Φύλλο Κρούστας Νωπό 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "434",
      "name": "Creta Farms Εν Ελλάδi Λουκάν Παραδ Χ Γλουτ 340γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "435",
      "name": "Γιώτης Super Mousse Κακ 234γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "436",
      "name": "Παπαδημητρίου Κρεμά Βαλσαμ Χ Γλ 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "437",
      "name": "Friskies Γατ/Φή Πατέ Κοτ/Λαχ 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "438",
      "name": "Νουνού Γάλα Family Υψ Θερ Επ Light 1,5% 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "441",
      "name": "Pummaro Κέτσαπ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "445",
      "name": "Αχλάδια Κρυσταλία Εγχ Εξτρα ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "446",
      "name": "Κρασί Της Παρέας Ροζέ Κοκκινέλι 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "447",
      "name": "Pedigree Schmackos Μπισκότα Σκύλου 43γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "449",
      "name": "Cheetos Pacotinia 114γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "451",
      "name": "Kerrygold Τυρί Regato Τριμ.400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "452",
      "name": "Ariel Alpine Υγρές Καψ 3σε1 24πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "454",
      "name": "Finish Αποσκλ/Κο Αλάτι Πλυν 2,5κιλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "455",
      "name": "Ντομάτες Εγχ Υδροπ Κατ  Β.  ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "456",
      "name": "7 Days Κέικ Bar Κακάο 5Χ30γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "468",
      "name": "Κύκνος Τοματοπολτός 28% Μεταλ 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5aba290bf919489da5810c6122f0bc9b"
    },
    {
      "id": "469",
      "name": "Δέλτα Advance Επιδ Αλεσμένα Δημητρ 2Χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "471",
      "name": "Syoss Cond Βαμμένα Μαλ 500ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "473",
      "name": "Τσανός Μουστοκούλουρα 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47b5f0016f4f0eb79e3a4b932f7577"
    },
    {
      "id": "474",
      "name": "Rilken Gel Χτεν Clubber 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "476",
      "name": "Σαβόϊ Βούτυρο Τύπου Κερκύρας 250gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "477",
      "name": "Μεβγάλ Πολίτικο 2Χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "478",
      "name": "Γιώτης Σοκολάτα Sweet/Balance Χ Γλουτ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "479",
      "name": "Fissan Baby Κρέμα 50γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "481",
      "name": "Persil Black Essenzia Απορ Υγρ 25πλ 1,5λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "482",
      "name": "Pampers Prem Care No5 11-18κιλ 30τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "484",
      "name": "Λακωνία Φυσικός Χυμός Πορτοκάλι 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "485",
      "name": "Lux Aφρόλ Magical Beauty 700ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "487",
      "name": "Φράουλες Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "488",
      "name": "Κρασί Της Παρέας Λευκό 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "493",
      "name": "Donna Οινόπνευμα Καθαρό 245ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "494",
      "name": "Soupline Mistral Μαλακτικό 13πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "499",
      "name": "Κανάκι Σφολιατ Χωρ Στρ Κουρού 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "502",
      "name": "Skip Υγρό Πλ Παν/Μικρ 26πλ 910ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "503",
      "name": "Μεβγάλ Γάλα «Κάθε Μέρα» 1.5% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "504",
      "name": "Το Μάννα Παξιμάδι Κρίθινο 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "505",
      "name": "Μπάρμπα Στάθης Αρακάς 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "506",
      "name": "Χρυσή Ζύμη Μπουγάτσα Θεσ/Κης Κρέμα 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "507",
      "name": "Fairy Original All in One Καψ Πλυντ Πιάτ Λεμόνι 22τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "508",
      "name": "Danone Activia Επιδ Γιαουρ Τραγ Απόλ 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "509",
      "name": "Υφαντής Σαλάμι Αέρος Χ Γλουτ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "511",
      "name": "Λακώνια Φυσ Χυμός Πορτοκάλι 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "515",
      "name": "Όλυμπος Τυρί Χωριάτικο Σε Άλμη 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "516",
      "name": "Μεβγάλ Παραδοσιακό Γιαούρτι Προβ 220γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "518",
      "name": "Quanto Μαλακτ Μη Συμπ Μπλε 2λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "519",
      "name": "La Vache Qui Rit Τυρί 8τμχ 140γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "520",
      "name": "Pillsbury Ζύμη Φρέσκια Σφολιάτας 700γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "521",
      "name": "Dixan Gel 30πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "522",
      "name": "Tasty Φουντούνια 105γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "f87bed0b4b8e44c3b532f2c03197aff9"
    },
    {
      "id": "523",
      "name": "Ρεπάνη Αγιωργίτικος Ερυθρός Οίνος 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "524",
      "name": "Gillette Fusion Proglide Power Ανταλ 3 τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "525",
      "name": "Παλίρροια Ντολμαδάκια Γιαλαντζί 280γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "528",
      "name": "Dove Αποσμ Σπρέυ 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "531",
      "name": "Adoro Βούτυρο 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "532",
      "name": "Alfa Ζύμη Για Πίτσα 600γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "533",
      "name": "Ήπειρος Φέτα Μαλακή 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "534",
      "name": "Τσιλιλή Τσίπουρο Χ Γλυκάνισο 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "535",
      "name": "La Vache Qui Rit Τυρί Φέτες Light 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "536",
      "name": "Pedigree Denta Stix Med Σκύλου 180γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "537",
      "name": "La Vache Qui Rit Τυρί Cheddar Φέτες 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "539",
      "name": "Kerrygold Τυρί Regato 270γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "540",
      "name": "Χρυσή Ζύμη Τυροπιτάκια 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "542",
      "name": "Βιτάμ Soft Μαργαρίνη 3/4 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "543",
      "name": "Υφαντής Χάμπουργκερ Top Burger 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "544",
      "name": "Γιώτης Κουβερτούρα Γαλακ Σταγ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "547",
      "name": "Neomat Total Eco Απορ Σκον 14πλ 700γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "548",
      "name": "Χρυσή Ζύμη Τυροπιτάκια Κουρου 920γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "549",
      "name": "Corona Μπύρα Extra 355ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "550",
      "name": "Μεβγάλ Γιαούρτι Πρόβειο Παραδ 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "551",
      "name": "Peppa Pig Φρουτοποτό Τροπ Φτούτα 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "552",
      "name": "Φάγε Τρικαλινό Τυρί Ζαρί Light Φάγε 380γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "554",
      "name": "Ρεπάνη Μοσχοφίλερο Λευκός Οίνος 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "555",
      "name": "Κύκνος Τοματάκι Ψιλοκ Χαρτ Συσκ 370γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "556",
      "name": "Φάγε Total Γιαούρτι Στραγγιστό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "559",
      "name": "Μεβγάλ Τριμμένο Τυρί Light 10% Λ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "561",
      "name": "Όλυμπος Γιαούρτι Στραγγ 10% Λ 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "562",
      "name": "Pantene Κρέμα Μαλλ Αναδόμησης 270ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "563",
      "name": "Danone Activia Επιδ Τραγαν Απολ Δημ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "564",
      "name": "Biofarma Παστέλι Βιολ Με Σουσάμι 30gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "566",
      "name": "Ζωγράφος Φρουκτόζη 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a885d8cd1057442c9092af37e79bf7a7"
    },
    {
      "id": "570",
      "name": "Friskies Γατ/Φή Πατέ Μοσχάρι 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "571",
      "name": "Persil Black Υγρό Απορ Πλυντ Ρούχ 12Μεζ 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "572",
      "name": "Pampers Prem Care No4 8-14κιλ 34τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "573",
      "name": "Whiskas Γατ/Φή Πουλ Σε Σάλτσα 100γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "575",
      "name": "Ήπειρος Τυρί Ελαφρύ Σε Άλμη 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "576",
      "name": "Νίκας Γαλοπ Καπνισ + Gouda Τυρί Light Φετ 280γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "577",
      "name": "Lenor Μαλακτικό Gold Orchid 26πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "578",
      "name": "Μινέρβα Χωριό Βούτυρο 41% Επαλ Σκαφ 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "579",
      "name": "Μπάρμπα Στάθης Μπάμιες Extra 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "580",
      "name": "Gillette Sensor Excel Ανταλ Ξυρ 5 τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "581",
      "name": "Βιτάμ Μαργαρίνη Soft Light 39% Λιπ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "582",
      "name": "Swiffer Πανάκια Αντ/Κα 16τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "583",
      "name": "Δέλτα Advance Επιδ Μπαν/Μηλο 2Χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "584",
      "name": "Δέλτα Smart Επιδ Γιαουρ Φραουλ 2Χ145γρ +1δώρο",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "585",
      "name": "Finish All In 1 Καψ Πλυντ Πιάτ Max Regular 27τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "586",
      "name": "Μεβγάλ Harmony Gourmet Πορτοκ Νιφ Σοκ 165γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "587",
      "name": "Νίκας Σαλάμι Αέρος 72 Πικάντ Χ Γλ 165γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "588",
      "name": "Pom Pon Μαντ Καθαρ Argan Oil 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "589",
      "name": "Sanitas Σακ Απορ Ultra 52Χ75cm 10τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "590",
      "name": "Del Monte Κομπόστα Ανανά Φέτες 565γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "591",
      "name": "Dove Σαπούνι 100γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "592",
      "name": "Dove Ντούς Deeply Nourisηing 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "593",
      "name": "Εβόλ Γάλα Παστερ Αγελαδ Βιολ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "595",
      "name": "Omo Υγρό Απορ Τροπ Λουλ 30πλ 1,95l",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "596",
      "name": "Head & Shoulders Σαμπουάν Total Care 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "597",
      "name": "Χρυσή Ζύμη Στριφταρi Τυρί Μυζ Μακεδον 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "598",
      "name": "Dixan Σκόνη Πλυντ 42πλ 2,31γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "599",
      "name": "Λεβέτι Κασέρι Ποπ Φέτες 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "600",
      "name": "Flora Μαργαρίνη Πλακ 70% Λιπ 25% 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "601",
      "name": "O.B. Ταμπόν Original Normal 16τμχ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "602",
      "name": "Βιτάμ Μαργαρίνη Κλασικό 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "603",
      "name": "Pampers Active Baby No5 11-16κιλ 51τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "604",
      "name": "Νίκας Λουκάν Φρανκ Γαλοπ Χ Γλ 280γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "605",
      "name": "Ariel Alpine Απορ Σκόνη 2,925γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "606",
      "name": "Klinex Υγρά Πανάκια 30τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "607",
      "name": "Βεμ Ρώσικη Σαλάτα 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4f205aaec31746b89f40f4d5d845b13e"
    },
    {
      "id": "608",
      "name": "Δέλτα Advance Επιδορπιο Λευκό 2χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "609",
      "name": "Nestle Ρόφημα Γαλακτ Junior 2+ Rtd 1λιτ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "610",
      "name": "Το Μάννα Παξιμάδια Λαδ Κυθήρων 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "611",
      "name": "Elvive Color Vive Γαλακτ Μαλ 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "612",
      "name": "Quaker Τραγανές Μπουκ Σοκολ Υγείας 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "613",
      "name": "Tsakiris Πατατάκια Αλάτι 72γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "615",
      "name": "Quaker Τραγ Μπουκ 4 Ξηροί Καρποί 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "616",
      "name": "Όλυμπος Γάλα Ζωής Λευκό Υψ Παστ 1,5% Λ 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "617",
      "name": "Kellogg's Special Κ 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "618",
      "name": "Lenor Gold Orchid 56μεζ 1,4λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "619",
      "name": "Soupline Mistral Μαλακτικό Συμπ 28πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "620",
      "name": "Ferrero Kinder Pingui Σοκ/Γκοφρ 4X124γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "621",
      "name": "Flora Maργαρίνη Soft 60% Λιπ 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "622",
      "name": "Johnson's Baby Μπατονέτες Βαμβ 100τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "624",
      "name": "Fina Τυρί Φέτες 10% Λιπ 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "626",
      "name": "Knorr Ρύζι Risonatto Milanaise 220γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "631",
      "name": "Forno Bonomi Μπισκ Σφολιατ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "632",
      "name": "Χρυσή Ζύμη Σπιτικά Τριγων Φέτα Κατικ 750γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "633",
      "name": "Μεβγάλ Ξινόγαλο 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "634",
      "name": "Becel Pro Activ Ρόφημα Γιαουρ Φράουλα 4Χ100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "635",
      "name": "Χρυσή Ζύμη Πίτσα Μαργαρίτα 2X470γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3f38edda7854447a837956d64a2530fa"
    },
    {
      "id": "636",
      "name": "Quanto Μαλακτ Ρουχ Ελλ Νησ 2λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "637",
      "name": "Δέλτα Γιαούρτι Μικ Οικ Φαρμ 2% 2Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "638",
      "name": "Μάσκα Προσ 10τεμ 1 Χρήση",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "640",
      "name": "Philadelphia Τυρί 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "641",
      "name": "Le Petit Marseillais Μάσκα Μαλλ Ξηρ 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "642",
      "name": "Tuboflo Αποφρακτικό Σκόνη Φάκελ 100g",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "643",
      "name": "Μεβγάλ Τριμμένο Σκληρό Τυρί 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "644",
      "name": "Ferrero Kinder Αυγό Εκπλ Χ Γλουτ 20γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "645",
      "name": "Babylino Sensitive No1 2-5κιλ 28τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "646",
      "name": "Becel Pro Activ Μαργαρίνη Σκαφ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "648",
      "name": "Ferrero Kinder Αυγό Εκπλ Χ Γλουτ 3τ 60γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "649",
      "name": "Champion Κρουασ Πραλίνα Φουντουκ 4X70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "650",
      "name": "Don Simon Kρασί Sangria Χαρτ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "651",
      "name": "Friskies Σκυλ/Φή Βοδ/Κοτ/Λαχ 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "653",
      "name": "Φάγε Τρικαλινό Τυρί Ζάρι Φάγε 380γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "654",
      "name": "Όλυμπος Γάλα Ζωής Πλήρες Υψ Παστ 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "655",
      "name": "ΣΟΥΡΩΤΗ Μεταλλικό Νερό Ανθρ Λεμον 330ml ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "656",
      "name": "Pemα Ψωμί Σικ Ολ Άλεσης 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "657",
      "name": "Skip Duo Καψ Πλυντ Ρούχ Active Clean 578γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "660",
      "name": "Tsakiris Πατατάκια Αλάτι 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "661",
      "name": "Ήπειρος Φέτα Ποπ Σε Άλμη 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "663",
      "name": "Knorr Μανιταρόσουπα 90γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eef696c0f874603a59aed909e1b4ce2"
    },
    {
      "id": "664",
      "name": "Φάγε Τυρί Τριμμένο Gouda 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "665",
      "name": "Lux Σαπούνι Soft/Creamy 125γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "666",
      "name": "Mini Babybel Τυρί Classic 10τεμ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "667",
      "name": "Tsakiris Πατατάκια Ρίγανη 72γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "669",
      "name": "Μεβγάλ Γάλα «Κάθε Μέρα» 3.5% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "670",
      "name": "Μίνι Babybel Διχτάκι 6τεμ 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "672",
      "name": "Γιαννιώτη Φύλλο Χωριατ Νωπό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "673",
      "name": "Activel Plus Αντισηπτικό Gel Χεριών 500ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "675",
      "name": "Orzene Condit Μπύρας Κανον Μαλλ 250ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "677",
      "name": "Gillette Fusion 5 Proglide Ξυρ Μηχ+Ανταλ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "678",
      "name": "Τσιλιλή Τσίπουρο Χ Γλυκάνισο 200ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "679",
      "name": "Knorr Quick Soup Μανιτ Με Κρουτόν 36γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eef696c0f874603a59aed909e1b4ce2"
    },
    {
      "id": "680",
      "name": "Κύκνος Τοματοχυμός 390ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "681",
      "name": "Becel Pro Activ Ελαιόλαδο 35% Λιπ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "685",
      "name": "Ζαγόρι Νερό Athletic 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "686",
      "name": "Johnson's 24η Κρ Ημ Essentials Hydr SPF15 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "687",
      "name": "Pillsbury Ζύμη Κρουασάν 230γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "688",
      "name": "Pillsbury Αφρατ Ζυμ Για Πίτσα 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "692",
      "name": "Όλυμπος Κεφαλοτύρι Προβ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "693",
      "name": "Κλεοπάτρα Σαπούνι 125γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "696",
      "name": "Βιτάμ Μαργαρίνη Soft Σκαφ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "697",
      "name": "Λάπα Νεαρού Μοσχ Α/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "698",
      "name": "Airwick Αντ/Κο Αποσμ Χώρου Βαν/Ορχιδ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "21051788a9ff4d5d9869d526182b9a5f"
    },
    {
      "id": "699",
      "name": "Fa Αφρόλ Yoghurt Van Honey 750m",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "700",
      "name": "Μάσκα Προσώπου Υφασμ 1τεμ",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "702",
      "name": "Κρεμμύδια Ξανθά Ξερά Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "703",
      "name": "Φάγε Κεφαλοτύρι Τριμμένο 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "704",
      "name": "Πέρκα Φιλέτο Κτψ Εισ Συσκ/Νη",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "708",
      "name": "Dorodo Τυρί Τριμμ Φακ 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "709",
      "name": "Gelita Ζελατίνη Φύλλα 20γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "710",
      "name": "Κρασί Της Παρέας Ερυθρό 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "711",
      "name": "Φάγε Μιγμ Tριμ 4 Τυρ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "713",
      "name": "Swiffer Dusters 5τεμ+Χειρολαβή",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "714",
      "name": "Μεβγάλ Τριμμένο Κεφαλοτύρι 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "715",
      "name": "Gillette Fusion Proglide 5+1 Ανταλ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "716",
      "name": "Έψα Λεμοναδα 232ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "717",
      "name": "Fissan Baby Ενυδατική κρέμα 150 ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "718",
      "name": "Ροδόπη Αριάνι 1,7% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "719",
      "name": "Swiffer Dusters Αντ/κα 10τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "720",
      "name": "Pyrox Εντομ/Ko Σπιράλ 20τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "8f98818a7a55419fb42ef1d673f0bb64"
    },
    {
      "id": "723",
      "name": "Στεργίου Λουκουμάς 4τεμ 340γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47b5f0016f4f0eb79e3a4b932f7577"
    },
    {
      "id": "725",
      "name": "Gillette Αφρός Ξυρ Sens Classic 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "726",
      "name": "Lactacyd Intimate Lotion Ευαίσθ Περιοχ 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "727",
      "name": "Wella New Wave Πηλός Γλυπτικής 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "729",
      "name": "Elnett Λακ Βαμμένα Μαλλ Satin 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "731",
      "name": "Everyday Σερβ Super/Ultra Plus Sens 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "732",
      "name": "Αύρα Νερό Μεταλ Μπλουμ 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "733",
      "name": "Παπουτσάνη Σαπούνι Πρασ Παραδ 125γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "734",
      "name": "Φλώρινα Ξυνό Νερό 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "735",
      "name": "Vidal Αφρόλ White Musk 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "736",
      "name": "Μεβγάλ Only 0% Et Συρτ 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "737",
      "name": "Nivea Baby Φυσιολογικός Ορός 24Χ5ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "738",
      "name": "Τεντούρα Κάστρο Λικέρ 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "739",
      "name": "Nivea Νερό Διφασ Ντεμακ Ματιών 125ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "740",
      "name": "OralB Χειρ Οδοντoβ 1/2/3 Clas Care 40 Med 2 τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "6db091264f494c86b9cf22a562593c82"
    },
    {
      "id": "741",
      "name": "Svelto Gel Υγρό Πιάτων Λεμόνι 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "742",
      "name": "Halls Καραμ Cool Menthol 28γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7cfe21f0f1944b379f0fead1c8702099"
    },
    {
      "id": "743",
      "name": "Sani Pants N2 Medium 14τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "0bf072374a8e4c40b915e4972990a417"
    },
    {
      "id": "744",
      "name": "Ultrex Σαμπουάν Γυναικ Κανον 360ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "745",
      "name": "Zest Familia Λουκανικοπιτάκια 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "746",
      "name": "Dettol Αντιβ Υγρό Κρεμοσ Ευαίσθ Επιδερμ Αντ/κο 250ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "747",
      "name": "Johnson's Baby Λοσιόν Bedtime 300ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "748",
      "name": "Ribena Φρουτοποτό Φραγκοστάφυλλο 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "750",
      "name": "Εύρηκα Σκόνη Antikalk 54γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "751",
      "name": "Grants Ουίσκι 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "752",
      "name": "Morfat Κρέμα Σαντιγύ Μετ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "753",
      "name": "Γιαννιώτη Φύλλο Κρουσ Νωπό 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "754",
      "name": "Texas Νιφάδες Βρώμης 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "755",
      "name": "Καλλιμάνης Χταπόδι Μικρό 595γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "756",
      "name": "Aim Οδ/τσα 2-6 Παιδική",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "6db091264f494c86b9cf22a562593c82"
    },
    {
      "id": "757",
      "name": "Hansaplast Φυσική Ελαφρόπετρα",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "a610ce2a98a94ee788ee5f94b4be82c2"
    },
    {
      "id": "759",
      "name": "Oral B Στοματικό Διαλ Δοντ/Ουλων 500ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "181add033f2d4d95b46844abf619dd30"
    },
    {
      "id": "760",
      "name": "Sani Υποσέντονα Fresh Maxi Plus 15τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "0bf072374a8e4c40b915e4972990a417"
    },
    {
      "id": "761",
      "name": "Nivea Μάσκα Μέλι για Ξηρ/Ευαίσθ Επιδ 2x7,5ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "762",
      "name": "Μινέρβα Χωριό Eλαιόλαδο Εξαιρ Παρθ 4λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "763",
      "name": "Μινέρβα Αραβοσιτέλαιο 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "764",
      "name": "Στάμου Γιαούρτι Πρόβειο Παραδ 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "765",
      "name": "Βλάχα Χυλοπιτάκι Με Αυγά 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "766",
      "name": "COVER 10τεμ Μάσκ Με Λάστιχο 1 Χρήση",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "767",
      "name": "Απαλαρίνα Λικέρ Μαστίχα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "768",
      "name": "Cool Hellas Χυμός Πορτοκαλ Συμπ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "769",
      "name": "McCain Πατάτες Tradition Σακ 1κλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5c5e625b739b4f19a117198efae8df21"
    },
    {
      "id": "770",
      "name": "Ροδόπη Γάλα Χ Λακτόζη 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "771",
      "name": "Proderm Kids Αφρόλουτρο Χαμομήλι 700ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "772",
      "name": "Μεβγάλ Παραδ Γιαούρτι Αιγοπρ Ελαφ 2Χ220γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "773",
      "name": "Gouda Τυρί Φάγε Φέτες 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "774",
      "name": "Καλλιμάνης Πέρκα Φιλέτο 595γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "775",
      "name": "Μινέρβα Ελαιόλαδο 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "776",
      "name": "Glade Αντ/Κο Αποσμ Χώρου Λεβάντα",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "21051788a9ff4d5d9869d526182b9a5f"
    },
    {
      "id": "777",
      "name": "Haribo Goldbaren Καραμ Ζελίνια Αρκουδ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7cfe21f0f1944b379f0fead1c8702099"
    },
    {
      "id": "778",
      "name": "OralB Οδ/Mα 1/2/3 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "779",
      "name": "Χρυσή Ζύμη Τυροπίτα Σπιτική 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "780",
      "name": "Ruffles Barbeque 130γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "781",
      "name": "Μεβγάλ Μανούρι 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "782",
      "name": "Χωριό Ελαιόλαδο Κορωνεική Ποικ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "783",
      "name": "EggPro Ροφ Πρωτεΐνης Φράουλα Χ Γλουτ 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "784",
      "name": "Svelto Gel Υγρό Πιάτων Με Ξύδι 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "786",
      "name": "Φάγε Total Γιαούρτι 5% 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "787",
      "name": "Οίνος Ερ Γλυκ Μαυροδάφνη Αχαΐα 375ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "788",
      "name": "Μεβγάλ Topino Απαχο Γάλα Κακάο 310ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "789",
      "name": "Παυλίδης Γκοφρέτα 3bit 31γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "790",
      "name": "Μεβγάλ Τριμμένο Σκλήρο Τυρί 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "791",
      "name": "Καλλιμάνης Καλαμαράκι Κομ Καθαρ 595γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "792",
      "name": "Τσίχλες Trident Δυόσμος 8γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7cfe21f0f1944b379f0fead1c8702099"
    },
    {
      "id": "793",
      "name": "Υφαντής Ζαμπόν Μπούτι Βραστό Σε Φέτες 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "794",
      "name": "Αλλοτινό Οίνος Ερυθρ Ημιγλυκ 0,5ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "795",
      "name": "Afroso Wc Block Τριαντ 2Χ40ΓΡ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "797",
      "name": "Κύκνος Κέτσαπ Top Down Χ Γλουτ 580γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "798",
      "name": "Λουξ Σόδα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "799",
      "name": "Ρούσσος Νάμα Κρασί Ερυθρό Γλυκο 375ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "800",
      "name": "Δέλτα Vitaline 0% Τρ Φρουτ/Δημ 380γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "801",
      "name": "Stella Artois Μπύρα 6x330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "802",
      "name": "Stella Artois Μπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "803",
      "name": "Μεβγάλ Φέτα Vacuum 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "804",
      "name": "Nivea Κρ Νύχτας Cellular Anti-Age 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "805",
      "name": "Purina One Γατ/Φή Ξηρά Βοδ/Σιτ 800γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "806",
      "name": "Garnier Νερό Ντεμακιγιάζ Micellaire 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "807",
      "name": "Dove Deodorant Κρέμα Rollon 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "808",
      "name": "Μεβγάλ Κρέμα Βανίλια 150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "809",
      "name": "Ζαναέ Ντολμαδάκια 280γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "810",
      "name": "Libresse Σερβ Goodnight Clip 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "811",
      "name": "Colgate Οδ/τσα Ext Clean Med Twin Pack",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "6db091264f494c86b9cf22a562593c82"
    },
    {
      "id": "812",
      "name": "Μεβγάλ Κεφίρ Lactose Free Με Ροδακ 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "813",
      "name": "Colgate Οδ/Μα Total Original 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "814",
      "name": "Fissan Baby Πούδρα 100gr",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "815",
      "name": "Hansaplast Universal Αδιάβροχα 40τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "1b59d5b58fb04816b8f6a74a4866580a"
    },
    {
      "id": "816",
      "name": "Flokos Σκουμπρί Φιλέτο Καπνιστό 160gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "817",
      "name": "Wella Flex Mousse Curles/Waves 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "818",
      "name": "Vanish Pink Πολυκαθαριστικό Λεκέδων 30γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "819",
      "name": "Veet Ταινίες Κρύο Κερί 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "820",
      "name": "Sensodyne Οδ/μα Complete Protection 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "821",
      "name": "Zewa Χαρ Υγείας Ultra Soft 8τεμ 912γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "822",
      "name": "Colgate Οδ/Μα Sensation Whiten.75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "823",
      "name": "Garnier Express Ντεμακιγιάζ Ματιών 2σε1 125ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "824",
      "name": "Bioten 24η Κρέμα Ενυδ 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "fefa136c714945a3b6bcdcb4ee9e8921"
    },
    {
      "id": "825",
      "name": "Μεβγάλ Κρεμα Σοκολάτα 150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "826",
      "name": "Χυμός Ρόδι/Μηλ/Καρ Χριστοδούλου 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "827",
      "name": "Babylino Sensitive No3 Econ 4-9κιλ 56τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "828",
      "name": "Εδέμ Φασόλια Κόκκινα Σε Νερό 240γρ.",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "829",
      "name": "Μύλοι Αγίου Γεωργίου Easy Bake Μειγ Muffin 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "830",
      "name": "Elvive Extraordinary Oil Universal 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "831",
      "name": "Friskies Adult Ξηρά Γατ/Φή Κουν/Κοτ/Λαχ 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "832",
      "name": "Friskies Adult Ξηρά Γατ/Φή Βοδ/Συκ/Κοτ 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "833",
      "name": "Friskies Σκυλ/Φή Ξηρ Κοτ/Λαχ 1,5κιλ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "834",
      "name": "Friskies Active Σκυλ/Φή Ξηρά Vital 1,5κιλ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "835",
      "name": "Gillette Venus Ξυρ Γυν Ανταλ 4τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "836",
      "name": "Regilait Γάλα Αποβ/Νο Σε Σκόνη 250γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "837",
      "name": "Bonne Maman Μαρμελάδα Φρα Χ Γλ.370γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "838",
      "name": "Bonne Maman Μαρμελάδα Βερικ Χ Γλ 370γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "839",
      "name": "Pedigree Υγ Σκυλ/Φή 3 Ποικ Πουλερικών 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "840",
      "name": "Pedigree Σκυλ/Φή Πατέ Κοτοπ/Μοσχ 300γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "841",
      "name": "Leerdammer Τόστ Light 10 φέτες 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "842",
      "name": "Bic Ξυρ Μηχ Classic 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "843",
      "name": "Purina Gold Gourmet Γατ/Φή Βοδ/Κοτ 85γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "844",
      "name": "Nestle Fitness Bars Σοκολάτα 6Χ23,5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "845",
      "name": "Nestle Nesquik 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "846",
      "name": "Nestle Cheerios 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "847",
      "name": "Nestle Cookie Crispies 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "848",
      "name": "Johnson's Baby Σαμπουάν 750ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "849",
      "name": "Johnson's Baby Oil Ενυδατικό Λάδι, 300ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "850",
      "name": "L'Oreal Σαμπ Elvive Color Vive Βαμμένα 400ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "851",
      "name": "Elvive Color Vive Μάσκα Μαλ 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "852",
      "name": "Botanic Therapy Σαμπουάν Επανόρθ 400ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "853",
      "name": "Philadelphia Τυρί Light 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "854",
      "name": "Philadelphia Τυρί 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "855",
      "name": "Dove Κρεμοσ/νο Ανταλ Regul 500ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "856",
      "name": "Kellogg's Coco Pops Chocos 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "857",
      "name": "Crunch Σοκολάτα Λευκή 100γρ Χωρίς Γλουτένη",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "858",
      "name": "Nestle Smarties Κουφετάκια Σοκολ 38γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "859",
      "name": "Hansaplast Universal Αδιάβροχα 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "1b59d5b58fb04816b8f6a74a4866580a"
    },
    {
      "id": "860",
      "name": "Nivea Κρέμα 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "861",
      "name": "Nivea Γαλάκτ Καθαρ Ξηρ/ Ευαίσθ Επιδ 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "862",
      "name": "Nivea After Shave Balsam 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "863",
      "name": "Nivea Κρέμα Ξυρίσματος 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "864",
      "name": "Atrix Κρέμα Χερ Intens Χαμομήλι 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "fefa136c714945a3b6bcdcb4ee9e8921"
    },
    {
      "id": "865",
      "name": "Nivea Αφρόλουτρο Cream Care 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "866",
      "name": "Nivea Visage Ημερ Kρ Απαλ Ενυδ Spf15 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "867",
      "name": "Nivea Κρ Ημέρας Ξηρ/Ευαίσθ Επιδ SPF15 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "868",
      "name": "Nivea Black/White Invisible 48h Rollon 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "869",
      "name": "Nivea After Shave Balsam Sens 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "870",
      "name": "Zewa Χαρτομάντηλα Soft/Strong 90τμχ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "871",
      "name": "Cesar Clasicos Σκυλ/Φή Μοσχ 150γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "872",
      "name": "Pedigree Σκυλ/Φή Μοσχάρι 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "873",
      "name": "Dr Beckmann Καθαρ Πλυν Ρούχ 250γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "874",
      "name": "Wella Flex Mousse Ultra Strong 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "875",
      "name": "Nutricia Biskotti 180γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "876",
      "name": "Pantene Σαμπουάν Αναδόμησης 360ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "877",
      "name": "Wella Koleston Βαφή Μαλ Ν7/77",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "09f2e090f72c4487bc44e5ba4fcea466"
    },
    {
      "id": "878",
      "name": "Omo Σκόνη 425γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "879",
      "name": "Fairy Υγρό Πιάτων Ultra Λεμόνι 900ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "880",
      "name": "Fairy Υγρό Πιάτων Ultra Κανονικό 900ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "881",
      "name": "Fairy Υγρό Πιάτων Ultra Classic 400ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "882",
      "name": "Vaseline Petroleum Jelly 100% Καθαρή Βαζελίνη 100 ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "fefa136c714945a3b6bcdcb4ee9e8921"
    },
    {
      "id": "883",
      "name": "Maggi Noodles Γεύση Κοτόπουλο 60γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eef696c0f874603a59aed909e1b4ce2"
    },
    {
      "id": "884",
      "name": "Quaker Νιφ Βρώμης Ολ Άλεσης 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "885",
      "name": "Sprite 6X330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "886",
      "name": "Dettol Αντιβ/κό Σπρέι 500ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "887",
      "name": "Brasso Γυαλιστικό Μετάλλων 150ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "888",
      "name": "Silvo Γυαλιστικό Ασημικών 150ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "889",
      "name": "Maltesers Κουφετάκια Σοκολ 37gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "890",
      "name": "Whiskas Γατ/Φή Κοτόπουλο 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "891",
      "name": "Autan Family Care Spray 100ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "8f98818a7a55419fb42ef1d673f0bb64"
    },
    {
      "id": "892",
      "name": "Johnnie Walker Ουίσκι Κόκκινο 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "893",
      "name": "Johnnie Walker Ουίσκι Black Label 12ετών",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "894",
      "name": "Dewar's Ουίσκι 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "895",
      "name": "Haig Ουίσκι 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "896",
      "name": "Gordons Space Τζιν Original 275ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "897",
      "name": "Gordon's Τζιν 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "898",
      "name": "Ballantines Ουίσκι 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "899",
      "name": "Durex Προφυλακτικά Jeans 12τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "7cfab59a5d9c4f0d855712290fc20c7f"
    },
    {
      "id": "900",
      "name": "Pedigree Denta Stix Small Σκύλου 110γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "901",
      "name": "Pedigree Rodeo Σκυλ/Φή Μοσχ 70γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "902",
      "name": "Cutty Sark Ουίσκι 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "903",
      "name": "Oral B Οδοντικό Νήμα Κηρωμένο 50τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "904",
      "name": "Bacardi Ρούμι 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "905",
      "name": "Martini Bianco Απεριτίφ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "906",
      "name": "Bailey's Irish Cream Λικέρ 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "907",
      "name": "Dettol All In 1 Πράσινο Μήλο 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "908",
      "name": "Finish Εκθαμβωτικό Υγρο Πλυν Πιάτ 400ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "909",
      "name": "Ίον Σοκολάτα Γάλακτος 45γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "910",
      "name": "Ίον Σοκολάτες Γάλακτος 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "911",
      "name": "Ίον Σοκολάτα Αμυγδάλου 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "912",
      "name": "Ίον Σοκολ Αμυγδ Υγείας 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "913",
      "name": "Ίον Κακάο 125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "914",
      "name": "Ίον Σοκοφρέτα Γάλακτος 38γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "915",
      "name": "Ίον Σοκοφρέτα Γάλακτ Με Φουντούκ 38γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "916",
      "name": "Ίον Σοκοφρέτα Σοκολ Υγείας 38γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "917",
      "name": "Ίον Σοκοφρέτα Μίνι Σακουλάκι 210γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "918",
      "name": "Derby Ίον 38γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "919",
      "name": "Heineken Μπύρα 6X330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "920",
      "name": "Monster Energy Drink 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "921",
      "name": "Danone Activia Επιδ Γιαουρ Ακτιν 2Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "922",
      "name": "Danone Activia Επιδ Γιαουρ Καρυδ/Βρώμη 2Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "923",
      "name": "Fix Hellas Mπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "924",
      "name": "Fix Hellas Μπύρα 6X330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "925",
      "name": "Γιώτης Ρυζόγαλο Στιγμής 105γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "926",
      "name": "Γιώτης Ανθός Αραβοσίτου Βανίλια 43γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "927",
      "name": "Γιώτης Αλεύρι Φαρίνα Κόκκινη 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "928",
      "name": "Γιώτης Μείγμα Για Κρέπες 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "929",
      "name": "Γιώτης Τούρτα Μιλφέιγ 532γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "930",
      "name": "Γιώτης Μαγιά 3φακ 8γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "931",
      "name": "Γιώτης Κρέμα Ζαχαροπλ Μιλφέιγ 170γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "932",
      "name": "Γιώτης Κορν Φλάουρ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "933",
      "name": "Γιώτης Σιρόπι Σοκολάτα 350γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "934",
      "name": "Γιώτης Κακάο 125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "935",
      "name": "Γιώτης Κουβερτούρα Σε Σταγόνες 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "936",
      "name": "Γιώτης Φρουιζελέ Φράουλα 2X100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "937",
      "name": "Γιώτης Φρουιζελέ Κεράσι Σε Σκ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "938",
      "name": "Γιώτης Κρέμα Ζαχαροπλ Βανίλια 117γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "939",
      "name": "Γιώτης Αλεύρι Για Όλες Τις Χρήσεις 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "940",
      "name": "Γιώτης Sanilac 3 Γάλα Σκόνη 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "941",
      "name": "Ούζο 12 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "942",
      "name": "Serkova Βότκα 37,5% 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "943",
      "name": "Παπαδοπούλου Caprice Ν6 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "35cce434592f489a9ed37596951992b3"
    },
    {
      "id": "944",
      "name": "Παπαδοπούλου Πτι Μπερ Ολικ Αλ 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "35cce434592f489a9ed37596951992b3"
    },
    {
      "id": "945",
      "name": "Παπαδοπούλου Μπισκότα Πτι Μπερ Ν16 225γ 16τεμ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "35cce434592f489a9ed37596951992b3"
    },
    {
      "id": "946",
      "name": "Παπαδοπούλου Μπισκότα Μιράντα Ν16 250γρ 12τεμ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "35cce434592f489a9ed37596951992b3"
    },
    {
      "id": "947",
      "name": "Παπαδοπούλου Krispies Σουσάμι 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "948",
      "name": "Παπαδοπούλου Krispies Ολικής Χωρίς Ζάχαρη 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "949",
      "name": "Παπαδοπούλου Κριτσίνια Μακεδ Ολ Αλ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "950",
      "name": "Παπαδοπούλου Ψωμί Σίτου Φυσ Προζύμι 700γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "951",
      "name": "Παπαδοπούλου Φρυγανιές Χωριάτικες 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "952",
      "name": "Amita Φυσικός Χυμός Πορτοκάλι 100% 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "953",
      "name": "Amita Motion Φυσικός Χυμός 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "954",
      "name": "Frulite Φρουτοπ Καροτ/Πορτ/Μαγκ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "955",
      "name": "Frulite Σαγκουίνι/Μανταρίνι 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "956",
      "name": "Frulite Φρουτοπoτό Πορτ/Βερικ 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "957",
      "name": "Amita Φρουτοποτό Πορ/Μηλ/Βερ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "958",
      "name": "Amita Motion Φυσικός Χυμός 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "959",
      "name": "Misko Τορτελίνι Με Τυρί 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "960",
      "name": "7 Days Τσουρεκάκι Κλασικό 75γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0e1982336d8e4bdc867f1620a2bce3be"
    },
    {
      "id": "961",
      "name": "Μίσκο Μακαρόνια Ν6 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "962",
      "name": "Misko Ταλιατέλλες Σιμιγδ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "963",
      "name": "Μίσκο Κριθαράκι Μέτριο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "964",
      "name": "Tasty Poppers Classic Ποπ Κορν 81γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8851b315e2f0486180be07facbc3b21f"
    },
    {
      "id": "965",
      "name": "Lay's Πατατάκια Ρίγανη150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "966",
      "name": "Klinex Χλωρίνη Classic 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "967",
      "name": "Klinex Χλωρίνη Classic 2λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "968",
      "name": "Klinex Χλωρίνη Lemon 2λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "969",
      "name": "Klinex Χλωρίνη Ultra Lemon 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "970",
      "name": "Klinex Χλωρίνη Ultra Lemon 1250ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "971",
      "name": "Aim Οδ/Μα Παιδ 2/6ετων 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "972",
      "name": "Aim Οδ/μα White System 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "973",
      "name": "Iglo Fish Sticks 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "974",
      "name": "Pummaro Χυμός Τομάτα Πιο Συμπ/Νος 520γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "975",
      "name": "Pummaro Χυμός Τομάτα 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "976",
      "name": "Pummaro Ψιλοκ Τοματ Κλασ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "977",
      "name": "Pummaro Χυμός Τομάτα Κλασικός 3Χ250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "978",
      "name": "Zwan Luncheon Meat 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "979",
      "name": "Life Χυμός Φυσικός Πορτοκάλι 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "980",
      "name": "Life Φρουτοποτό Πορτοκ/Μηλ/Καροτ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "981",
      "name": "Life Φρουτοπ Κρανμπ/Ρασμπ/Μπλουμπ 1lt",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "982",
      "name": "Life Φρουτοποτό Πορτ/Μηλ/Καρ 400ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "983",
      "name": "Δέλτα Φυσικ Χυμός Smart Ροδ Βερ200ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "984",
      "name": "Becel Pro Activ Ρόφημα Με Γαλ 1,8% Λ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "985",
      "name": "Jannis Παστέλι Σουσάμι Χ Γλ 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "986",
      "name": "Βέρμιον Νάουσα Κομπόστα Ροδάκινο 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "987",
      "name": "Μακεδονικό Ταχίνι Σε Βάζο 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "988",
      "name": "Κάλας Αλάτι Θαλασσινό Κλασικό 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "989",
      "name": "Ήρα Αλάτι Ψιλό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "990",
      "name": "Cair Αφρώδης Λευκός Ημίξηρος Οίνος 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "991",
      "name": "Φάγε Total Γιαούρτι Στραγγιστό 2% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "992",
      "name": "Τρικαλινό Τυρί Φάγε Ελαφ.Φετ.200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "993",
      "name": "Φάγε Τυρί Flair Cottage 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "994",
      "name": "Φάγε Γιαούρτι Αγελαδίτσα 4% 3χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "995",
      "name": "Φάγε Total Γιαούρτι 2% 3x200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "996",
      "name": "Φάγε Total Γιαούρτι 5% Φάγε 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "997",
      "name": "Φάγε Γιαούρτι Αγελάδος 2% Λ 3X200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "998",
      "name": "Παυλίδης Σοκολάτα Υγείας Αμύγδ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "999",
      "name": "Παυλίδης Σοκολάτα Υγείας Ν11 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1000",
      "name": "Fytro Σόγια Κιμάς 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1001",
      "name": "Fytro Ζάχαρη Καστανή Ακατέργαστη 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a885d8cd1057442c9092af37e79bf7a7"
    },
    {
      "id": "1002",
      "name": "Μιμίκος Κοτόπουλο Φιλ Μπούτ Νωπό Τυποπ 650γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "463e30b829274933ab7eb8e4b349e2c5"
    },
    {
      "id": "1003",
      "name": "Μιμίκος Κοτόπουλο Στηθ Φιλ Νωπό Τυποπ 845γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "463e30b829274933ab7eb8e4b349e2c5"
    },
    {
      "id": "1004",
      "name": "Κανάκι Φύλλο Κρούστας 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "1005",
      "name": "Κύκνος Τοματά Τριμμενη 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1006",
      "name": "Κύκνος Τοματοπολτός 410γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5aba290bf919489da5810c6122f0bc9b"
    },
    {
      "id": "1007",
      "name": "Κύκνος Κέτσαπ Χ Γλουτ 330γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1008",
      "name": "Κύκνος Τοματοπολτός 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5aba290bf919489da5810c6122f0bc9b"
    },
    {
      "id": "1009",
      "name": "Κύκνος Τομάτες Αποφλ Ολoκλ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1010",
      "name": "Κύκνος Χυμ Τομάτας Συμπ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1011",
      "name": "Κύκνος Τομάτα Ψιλ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1012",
      "name": "Knorr Κυβοι Λαχανικών 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "1013",
      "name": "Hellmann's Μουστάρδα Απαλή 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "1014",
      "name": "Hellmann's Μουστάρδα Απαλή 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "1015",
      "name": "Hellmann's Σαλάτα Φάρμα Κηπ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4f205aaec31746b89f40f4d5d845b13e"
    },
    {
      "id": "1016",
      "name": "Μεβγάλ Αριάνι 1,5% Χ Γλουτ 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1017",
      "name": "Μεβγάλ Κεφίρ 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1018",
      "name": "Μεβγάλ Creme Καραμελέ 150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "1019",
      "name": "Μεβγάλ Παραδοσιακό Γιαούρτι Αγελαδ 220γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1020",
      "name": "Μεβγάλ Τριμμενη Μυζήθρα Ξηρή 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1021",
      "name": "Μεβγάλ Ανθότυρο Τυποπ 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1022",
      "name": "Μεβγάλ Κεφίρ Φράουλα 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1023",
      "name": "Μεβγάλ High Protein Vanilla Drink 242ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1024",
      "name": "Μεβγάλ High Protein Choc Drink 242ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1025",
      "name": "Μεβγάλ Παραδοσιακό Γιαούρτι Κατσικ 220γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1026",
      "name": "Μεβγάλ Only Lact Free 1,5% 1λτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1027",
      "name": "Μεβγάλ High Protein Φρα Drink 237ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1028",
      "name": "Μεβγάλ Harmony 1% Με Μέλι/Γκραν 164γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1029",
      "name": "Αττική Μέλι 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "1030",
      "name": "Αττική Μέλι 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "1031",
      "name": "L'Oreal Studio Line Fx Gel Extra Fix 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "1032",
      "name": "L'Oreal Κρέμα Προσ Καν/Μικτ Επιδ 3 Φρον 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "1033",
      "name": "Μινέρβα Χωριό Φέτα Ποπ Βιολ Άλμη 350γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1034",
      "name": "Scotch Brite Σύρμα Πράσινο Κουζίνας",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1035",
      "name": "Scotch Brite Σφουγγ Κουζ Γίγας Αντιβ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1036",
      "name": "Scotch Brite Σφουγγαράκι Πράσ Κλασ 1τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1037",
      "name": "Εύρηκα Λευκαντικό 60γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1038",
      "name": "Topine Υγρό Επιφ Red Pine 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1039",
      "name": "Syoss Σαμπ Όγκο 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1040",
      "name": "Lipton Ice Tea Green No Sugar 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1041",
      "name": "Δωδώνη Τυρί Φέτα 400γρ Σε Άλμη",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1042",
      "name": "Όλυμπος Ταχίνι Χ Γλουτ 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1043",
      "name": "Μέλισσα Σπαγγέτι Ν6 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1044",
      "name": "Melissa Σιμιγδάλι Χονδρό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "1045",
      "name": "Μέλισσα Τορτελίνια Γεμ Τυρίων 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1046",
      "name": "Κορπή Νερό 6Χ1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "1047",
      "name": "Κορπή Νερό 6χ0,5ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "1048",
      "name": "Λουμίδης Καφές Ελληνικός 96γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1049",
      "name": "Λουμίδης Καφές Ελληνικός 194γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1050",
      "name": "Λουμίδης Καφές Ελληνικός 490γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1051",
      "name": "Nescafe Classic Στιγμιαίος Καφές 50γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1052",
      "name": "Nescafe Classic Στιγμιαίος Καφές 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1053",
      "name": "Nescafe Classic Στιγμιαίος Καφές 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1054",
      "name": "Friskies Άμμος Υγιεινής 5κιλ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "1055",
      "name": "Χρυσή Ζύμη Χορτοπίτα Σπιτική 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1056",
      "name": "Χρυσή Ζύμη Κασερόπιτα Σπιτική 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1057",
      "name": "Χρυσή Ζύμη Σφολιάτα 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "1058",
      "name": "Κουρτάκη Ρετσίνα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "1059",
      "name": "Amstel Μπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1060",
      "name": "Amstel Μπύρα 6Χ330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1061",
      "name": "Amstel Μπύρα 4X500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1062",
      "name": "Heineken Μπύρα 4X500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1063",
      "name": "Heineken Μπύρα Premium Lager 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1064",
      "name": "Heineken Μπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1065",
      "name": "Heineken Μπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1066",
      "name": "Άλφα Μπύρα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1067",
      "name": "Μηλοκλέφτης Μηλίτης 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1068",
      "name": "Μπάρμπα Στάθης Σπανάκι Φύλλα 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "1069",
      "name": "Μπάρμπα Στάθης Σαλάτα Καλαμπ 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "1070",
      "name": "Μπάρμπα Στάθης Αρακάς Λαδερός 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "1071",
      "name": "Μπάρμπα Στάθης Ρύζι Με Καλαμπόκι 600γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "1072",
      "name": "Μπάρπα Στάθης Τομάτα Στον Τρίφτη 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1073",
      "name": "Everyday Σερβ/Κια XL All Cotton 24τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1074",
      "name": "Everyday Σερβ Extr Long/Ultra Plus Hyp 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1075",
      "name": "Everyday Σερβ Extr Long/Ultra Plus Sens 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1076",
      "name": "Everyday Σερβ Norm/Ultra Plus Hyp 18τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1077",
      "name": "Everyday Σερβ Super/Ultra Plus Hyp 18 τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1078",
      "name": "Everyday Σερβ Maxi Nig/Ultra Plus Hyp 18τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1079",
      "name": "Everyday Σερβ Norm/Ultra Plus Sens 18τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1080",
      "name": "Everyday Σερβ Super/Ultra Plus Sens 18τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1081",
      "name": "Everyday Σερβ Maxi Nig/Ultra Plus Sens 18τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1082",
      "name": "Everyday Σερβ/Κια Norm All Cotton 24τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1083",
      "name": "Pom Pon Μαντηλ Ντεμακ Sensit 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "1084",
      "name": "Pom Pon Eyes & Face Μαντηλάκια 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "1085",
      "name": "Babycare Μωροπ/τες Αντ/κο 3Χ72τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "92680b33561c4a7e94b7e7a96b5bb153"
    },
    {
      "id": "1086",
      "name": "Everyday Σερβ Maxi Nig/Ultra Plus Sens 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1087",
      "name": "Everyday Σερβ Norm/Ultra Plus Sens 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1088",
      "name": "EveryDay Natural Fresh Υγρό Ευαίσθ Περιοχ 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1089",
      "name": "Babylino Sensitive No4 Econ 7-18κιλ 50τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "1090",
      "name": "Babylino Sensitive No5 Econ 11-25κιλ 44τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "1091",
      "name": "Sani Πάνα Ακρατ Sensitive N4 Xlarge 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "0bf072374a8e4c40b915e4972990a417"
    },
    {
      "id": "1092",
      "name": "Sani Lady Sensitive Super N5 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "0bf072374a8e4c40b915e4972990a417"
    },
    {
      "id": "1093",
      "name": "Μέγα Βαμβάκι 100γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "af538008f3ab40989d67f971e407a85c"
    },
    {
      "id": "1094",
      "name": "Daκor Corned Beef Μοσχάρι 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "1095",
      "name": "Σουρωτή Ανθρακούχο Φυσικό Νερό 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "1096",
      "name": "Μίνι Ούζο Επομ 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1097",
      "name": "Μίνι Ούζο Γλυκάνισο 200ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1098",
      "name": "Absolut Βότκα 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1099",
      "name": "Mythos Μπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1100",
      "name": "Tuborg Σόδα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1101",
      "name": "Υφαντής Ferano Προσούτο Χ Γλουτ 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1102",
      "name": "Υφαντής Μπουκιές Κοτόπουλο Κτψ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "1103",
      "name": "Υφαντής Μπέικον Καπνιστό Χ Γλουτ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1104",
      "name": "Υφαντής Κεφτεδάκια Κτψ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "1105",
      "name": "Υφαντής Λουκάνικα Βιέννα Αποφλ Χ Γλουτ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1106",
      "name": "Υφαντής Πίτσα Rock N Roll 3Χ460γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3f38edda7854447a837956d64a2530fa"
    },
    {
      "id": "1107",
      "name": "Camel Υγρο Δερμα Παπουτσιών Μαύρο 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "a610ce2a98a94ee788ee5f94b4be82c2"
    },
    {
      "id": "1108",
      "name": "Noxzema Αφρόλ Talc 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1109",
      "name": "Noxzema Αφρός Ξυρισ Xtr Sens 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "1110",
      "name": "Orzene Σαμπουάν Μπύρας Κανον 400ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1111",
      "name": "Pyrox Εντομ/Κο Σπιράλ 10τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "8f98818a7a55419fb42ef1d673f0bb64"
    },
    {
      "id": "1112",
      "name": "Ava Υγρό Πιάτων Perle Classic 900ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1113",
      "name": "Noxzema Αποσμ Rollon Classic 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "1114",
      "name": "Palmolive Υγρό Πιάτων Regular 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1115",
      "name": "Ava Υγρό Πιάτων Ξύδι/Μήλο/Μέντα 430ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1116",
      "name": "Sanitas Αλουμινόχαρτο 10μετ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1117",
      "name": "Sanitas Αντικολλητικό Χαρτί 8μετ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1118",
      "name": "Sanitas Αλουμινόχαρτο 30μ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1119",
      "name": "Sanitas Μεμβράνη Διάφανη 30μετ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1120",
      "name": "Sanitas Παγοκυψέλες 2 Σε 1",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1121",
      "name": "Rol Σκόνη Για Πλυσ Στο Χέρι 380γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1122",
      "name": "Trata Σαρδέλα Λαδιού 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "1123",
      "name": "Trata Σαρδέλα Πικάντικη 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "1124",
      "name": "Flokos Καλαμάρια Φυσ Χυμού 370γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "1125",
      "name": "Dettol Κρεμ Sensitive Αντ/κο 750ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "1126",
      "name": "Dettol Κρεμ Relax Αντ/κο 750ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "1127",
      "name": "Calgon Gel 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1128",
      "name": "Dettol Απολυμαντικό Για Ρούχα",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1129",
      "name": "Calgon Ταμπλέτες 15τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1130",
      "name": "Airwick Αποσμ Χώρου Stick Up 120γρ 2τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "21051788a9ff4d5d9869d526182b9a5f"
    },
    {
      "id": "1131",
      "name": "Vanish Oxi Action Ενισχ Πλύσης 500γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1132",
      "name": "7 Days Κρουασάν Κακάο 3Χ70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "1133",
      "name": "Palmolive Υγρό Πιάτων Λεμόνι 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1134",
      "name": "Ajax Kloron 2σε1 Λεμόνι 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1135",
      "name": "Ajax Τζαμιών 450ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1136",
      "name": "Neomat Total Eco Απορ Τριαν 14πλ 700γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1137",
      "name": "Vapona Σκοροκτόνα Φύλλα 20τμχ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "8f98818a7a55419fb42ef1d673f0bb64"
    },
    {
      "id": "1138",
      "name": "Persil Express Σκόνη Χεριού 420γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1139",
      "name": "Palette Λακ Πολύ Δυνατή 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "1140",
      "name": "Palette Βαφή Μαλ Ξανθό N8",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "09f2e090f72c4487bc44e5ba4fcea466"
    },
    {
      "id": "1141",
      "name": "3 Άλφα Φασόλια Μέτρια 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "1142",
      "name": "3 Άλφα Φακές Ψιλές Εισαγωγής 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "1143",
      "name": "Dirollo Τυρί Cottage 2,2% Λιπ 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1144",
      "name": "Ζωγράφος Μαρμελ Φράουλ Φρουκτ 415γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "1145",
      "name": "Ζωγράφος Μακαρόνια Διαίτης Ν6 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1146",
      "name": "Ζωγράφος Καστανή Ζάχαρη 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a885d8cd1057442c9092af37e79bf7a7"
    },
    {
      "id": "1147",
      "name": "Elite Φρυγανιές Σταριού Κουτί 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "1148",
      "name": "Elite Φρυγανιά Τρίμμα 180γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "1149",
      "name": "Κρις Κρις Ψωμί Τοστ Σταρένιο 700gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "1150",
      "name": "Αρκάδι Σαπούνι Πλάκα Πρασ 4Χ150γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "1151",
      "name": "Αρκάδι Υγρό Πλυντ Baby Με Σαπούνι 26πλυς",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "991276688c8c4a91b5524b1115122ec1"
    },
    {
      "id": "1152",
      "name": "Agrino Ρύζι Parboiled Bella Χ Γλουτ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "1153",
      "name": "Agrino Ρύζι Basmati Χ Γλουτ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "1154",
      "name": "Agrino Ρύζι Bella Parboiled Χ Γλουτ 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "1155",
      "name": "Bravo Καφές Κλασικός 95γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1156",
      "name": "Μύλοι Αγίου Γεωργίου Αλεύρι Για Όλες Τις Χρ 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "1157",
      "name": "Λάβδας Καραμέλες Βούτυρου 0% Ζαχαρ 32γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7cfe21f0f1944b379f0fead1c8702099"
    },
    {
      "id": "1158",
      "name": "Μαλαματίνα Ρετσίνα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "1159",
      "name": "Ζαγόρι Νερό 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "1160",
      "name": "Τοπ Ξύδι Κοκκίνου Κρασιού 350ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "1161",
      "name": "Καραμολέγκος Ψωμί Τοστ Σταρένιο 680γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "1162",
      "name": "Καραμολέγκος Ψωμί Τοστ Σταρένιο Μίνι 340g",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "1163",
      "name": "Καραμολέγκος Πίτες Για Σουβλ Σταρεν 10τεμ 820γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1164",
      "name": "Vileda Style Κουβάς",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1165",
      "name": "Tuborg Club Σόδα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1166",
      "name": "Στεργίου Μηλόπιτα Ατομική 105γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47b5f0016f4f0eb79e3a4b932f7577"
    },
    {
      "id": "1167",
      "name": "Όλυμπος Γάλα Κατσικίσιο Hπ 3,5% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1168",
      "name": "Όλυμπος Βούτυρο Αγελ Πακ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1169",
      "name": "Όλυμπος Γιαούρτι Στρ 2% Freelact 2Χ170γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1170",
      "name": "Όλυμπος Γιαούρτι Στραγγιστό 2% Λιπ 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1171",
      "name": "Όλυμπος Γιαούρτι Στραγγιστό 2% 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1172",
      "name": "Όλυμπος Φυσικός Χυμός Πορτοκάλι 1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1173",
      "name": "Όλυμπος Γάλα Επιλεγμ. 3,7% Λ 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1174",
      "name": "Όλυμπος Γάλα Επιλεγμ 1,5% Λ 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1175",
      "name": "Όλυμπος Φυσικός Χυμός Πορτοκάλι 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1176",
      "name": "Όλυμπος Φυσικός Χυμός Πορτ 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1177",
      "name": "Όλυμπος Φυσ Χυμός Μηλ Πορτ Kaρότο 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1178",
      "name": "Λουξ Πορτοκαλάδα Μπλε 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1179",
      "name": "Λουξ Πορτοκαλάδα Ανθρ 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1180",
      "name": "Λουξ Λεμονάδα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1181",
      "name": "Wella Flex Σπρέυ Ultra Strong 250ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "1182",
      "name": "Πλωμάρι Ούζο 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1183",
      "name": "Alfa Φύλλο Χωριάτικο Κιχι Κτψ 750γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1184",
      "name": "Alfa Κιχι Παραδοσιακή Πίτα Με Τυρί 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1185",
      "name": "Alfa Μπουγάτσα Θες/νίκης Κρέμα 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "1186",
      "name": "Creta Farms Λουκαν Χωριατ Μυρ Χ Γλουτ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1187",
      "name": "Creta Farms Εν Ελλάδι Κεφτεδάκια Κτψ 420γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "1188",
      "name": "Creta Farms Εν Ελλάδι Κοτομπουκιές Κτψ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "1189",
      "name": "Εν Ελλάδι Γαλοπούλα Καπνιστή Φέτες 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "1190",
      "name": "Μεταξά 3 Μπράντυ 350ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1191",
      "name": "Μεταξά 3 Μπράντυ 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1192",
      "name": "Βεργίνα Μπύρα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1193",
      "name": "Ροδόπη Γιαούρτι Πρόβειο Βιο 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1194",
      "name": "Ροδόπη Γιαούρτι Κατσικίσιο 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1195",
      "name": "Ροδόπη Γιαούρτι Πρόβειο 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1196",
      "name": "Καλλιμάνης Γλώσσα Φιλέτο 595γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "1197",
      "name": "Skip Σκόνη Regular 45πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1198",
      "name": "Καλλιμάνης Γαρίδες Αποφλ Μικρές 425γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "1199",
      "name": "Pillsbury Σάλτσα Για Πίτσα 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "1200",
      "name": "Jumbo Σνακ Γαριδάρες 85gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "f87bed0b4b8e44c3b532f2c03197aff9"
    },
    {
      "id": "1201",
      "name": "Στεργίου Τσουρέκι 380γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0e1982336d8e4bdc867f1620a2bce3be"
    },
    {
      "id": "1202",
      "name": "Στεργίου Κέικ Ανάμεικτο 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "1203",
      "name": "Δομοκού Τυρί Κατίκι Ποπ 200g",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1204",
      "name": "Green Cola 1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1205",
      "name": "Green Cola 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1206",
      "name": "Νουνού Γάλα Family 3,6% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1207",
      "name": "Νουνού Γάλα Family 1,5% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1208",
      "name": "Νουνού Γάλα Family 3,6% 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1209",
      "name": "Νουνού Κρέμα Γάλακτος Πλήρης 2Χ330ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4e4cf5616e0f43aaa985c1300dc7109e"
    },
    {
      "id": "1210",
      "name": "Sol Ηλιέλαιο 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "1211",
      "name": "Φλώρα Αραβοσιτέλαιο 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "1212",
      "name": "Νέα Φυτίνη Φυτικό Μαγειρικό Λίπος 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1213",
      "name": "Amstel Μπύρα Premium Quality 0,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1214",
      "name": "Axe Αφροντούς Africa 400ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1215",
      "name": "OralB Οδ/Μα Pro Exp Prof Prot 75m",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "1216",
      "name": "Alpro Ρόφημα Αμύγδαλο Χ Γλουτ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1217",
      "name": "Tide Alpine Απορ Χεριού Σκόνη 450γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1218",
      "name": "Coca Cola 1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1219",
      "name": "Fanta Πορτοκαλάδα 1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1220",
      "name": "Sprite Αναψυκτικό 1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1221",
      "name": "Coca Cola Zero 2Χ1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1222",
      "name": "Coca Cola Πλαστ 4Χ500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1223",
      "name": "Coca Cola 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1224",
      "name": "Coca Cola Zero 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1225",
      "name": "Sprite 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1226",
      "name": "Coca Cola Zero 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1227",
      "name": "Coca Cola Light 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1228",
      "name": "Coca Cola 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1229",
      "name": "Coca Cola 6Χ330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1230",
      "name": "Coca Cola 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1231",
      "name": "Coca Cola 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1232",
      "name": "L'Oreal Excellence Βαφή Μαλ Ξανθό Ν7",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "09f2e090f72c4487bc44e5ba4fcea466"
    },
    {
      "id": "1233",
      "name": "Lipton Χαμομήλι Φακ 10τεμΧ1γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "1234",
      "name": "Lurpak Soft Μειωμέν Λιπαρ Ανάλ 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1235",
      "name": "Lurpak Soft Αλατισμένο 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1236",
      "name": "Lurpak Βούτυρο Αναλ Αλουμ 125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1237",
      "name": "Lurpak Βούτυρο Ανάλατο 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1238",
      "name": "Vanish Σαμπουάν Χαλιών 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1239",
      "name": "Nestle Nesquik Ρόφημα Σακούλα 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "1240",
      "name": "Tena Lady Maxi 12τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1241",
      "name": "Zewa Χαρτί Κουζίνας Με Σχέδια 2τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "1242",
      "name": "Jose Cuervo Τεκίλα Espec Κιτρ 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1243",
      "name": "Nestle Fitness Dark Chocolate 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "1244",
      "name": "Nescafe Cappuccino 10φακ 140γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1245",
      "name": "Nestle Fitness 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "1246",
      "name": "Nescafe Azera Καφές Espresso 100% Arabica 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1247",
      "name": "Nescafe Dolce Gusto Cappuccino 16 Καψ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1248",
      "name": "Nescafe Dolce Gusto Espresso Int Καψ 16x7γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1249",
      "name": "Παυλίδης Μέρεντα Με Φουντούκι 570γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "1250",
      "name": "Παυλίδης Μερέντα 360γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "1251",
      "name": "Παυλίδης Κουβερτούρα Κλασ 125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1252",
      "name": "Παυλίδης Kiss Σοκολάτα Γάλ Φράουλα 27,5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1253",
      "name": "Παυλίδης Γκοφρέτα Υγείας 34γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1254",
      "name": "Παυλίδης Σοκολατα Υγειας Πορτοκ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1255",
      "name": "Canderel Υποκατάστατο Ζάχαρης 120 Δισκία",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a885d8cd1057442c9092af37e79bf7a7"
    },
    {
      "id": "1256",
      "name": "Gillette Venus Close&Clean+2 Ανταλ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1257",
      "name": "Gillette Gel Ξυρ Μοιsture 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "1258",
      "name": "Gillette Blue Ii Plus Slalom Sensit 5τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1259",
      "name": "Gillette Blue Ii Fixed Head 5τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1260",
      "name": "Gilette Ξυρ Μ/Χ Blue II Slalom 5τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1261",
      "name": "Gillette Fusion Αντ/κα Ξυραφ 4τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1262",
      "name": "Campari Bitter Aπεριτίφ 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1263",
      "name": "Lavazza Καφές Rossa Espresso 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1264",
      "name": "Ferrero Rocher Πραλίνες 16τεμ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1265",
      "name": "Ferrero Kinder Γάλακτοφέτες 5Χ140γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1266",
      "name": "Ferrero Kinder Σοκολ 2πλη 16τεμ Χ Γλουτ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1267",
      "name": "Asti Martini Αφρώδης Οίνος 0,75λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "1268",
      "name": "Lipton Τσάι Ρόφημα 10 Φακ 1,5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "1269",
      "name": "Lipton Τσάι Κίτρινο Φακ 20τεμΧ1,5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "1270",
      "name": "Lipton Ice Tea Instant Λεμονι 125γρ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1271",
      "name": "Pantene Μάσκα Μαλ Αναδόμησης 2λεπτ 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "1272",
      "name": "Always Σερβ Ultra Platinum Night 6τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1273",
      "name": "Always Σερβ Ultra Platinum Night 12τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1274",
      "name": "Ace Gentile Ενισχυτικό Πλύσης 1lt",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1275",
      "name": "Ace Gentile Ενισχυτικό Πλύσης 2lt",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1276",
      "name": "Always Σερβ Night 9τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1277",
      "name": "Veet Αποτριχωτική Κρέμα Κανον Επιδερμ 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1278",
      "name": "Veet Κρέμα Για Ευαίσθ Επιδ 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1279",
      "name": "Veet Κρύο Κερι Ταινίες Προσώπου 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1280",
      "name": "Omo Bianco Υγρό Αφρ Μασ Παραδοσ 30πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1281",
      "name": "Rio Mare Τόνος Νερόυ 2Χ160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "1282",
      "name": "Rio Mare Τόνος Λαδιού 2Χ160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "1283",
      "name": "Overlay Κρέμα Επίπλων 250ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1284",
      "name": "Overlay Επίπλων Σπρέυ 250ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1285",
      "name": "Fornet Καθαρ Φούρνου 300ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1286",
      "name": "Meritο Spray Σιδερώματος 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1287",
      "name": "Omino Bianco Υγρό Blacκ Wash 25πλ 1,5λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1288",
      "name": "Ferrero Kinder Bueno Σοκ/Τα 43γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1289",
      "name": "Kellogg's Corn Flakes 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "1290",
      "name": "Bref Power Active Wc Block Ωκεαν 50γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1291",
      "name": "Sensodyne Οδ/μα Repair/Protect 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "1292",
      "name": "Ferrero Kinder Σοκολ Bars Χ Γλουτ 8τ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1293",
      "name": "Purina Gold Gourmet Γατ/Φή Μους Ψάρι 85γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "1294",
      "name": "Barilla Μακαρόνια Ν5 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1295",
      "name": "Barilla Λαζάνια Με Αυγά 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1296",
      "name": "Barilla Πένες Rigate Νο 73 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1297",
      "name": "Barilla Σάλτσα Βασιλικος 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "1298",
      "name": "Barilla Σάλτσα Pesto Alla Genovese 190γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "1299",
      "name": "Barilla Μακαρ Linguine Bavette Ν13 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1300",
      "name": "Airwick Αντ/Κο Freshmatic Βαν/Ορχιδ 250ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "21051788a9ff4d5d9869d526182b9a5f"
    },
    {
      "id": "1301",
      "name": "Syoss Hairspray Max Ultra Strong 400ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "1302",
      "name": "Gliss Condition Ultimate Color 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "1303",
      "name": "Chupa Chups Melody Γλυφιτζ 12γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7cfe21f0f1944b379f0fead1c8702099"
    },
    {
      "id": "1304",
      "name": "Palmolive Κρεμ Μέλι Γάλα Αντ/κο 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "1305",
      "name": "Quaker Νιφ Βρώμης Ολ Άλεσης Μεταλ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "1306",
      "name": "McCain Πατάτες Mediterannean 750γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5c5e625b739b4f19a117198efae8df21"
    },
    {
      "id": "1307",
      "name": "Skip Υγρό Regular 30πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1308",
      "name": "Axe Αποσμητικό Σπρέυ Africa 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "1309",
      "name": "Omo Σκόνη Πλυντ Τροπ Λουλούδια 45πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1310",
      "name": "Fissan Baby Bagnetto Υποαλ Σαμπουάν/Αφρόλ 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "1311",
      "name": "Fissan Baby Σαπούνι 90γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "1312",
      "name": "Proderm Σαμπουάν/Αφρόλουτρο 1-3 400ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "1313",
      "name": "Milner Τυρί Φέτες 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1314",
      "name": "Νουνού Gouda Φέτες 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1315",
      "name": "Νουνού Τυρί Γκουντα Light 11% Φετ 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1316",
      "name": "Jacobs Καφές Φίλτρου Εκλεκτός 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1317",
      "name": "Jacobs Καφές Φίλτρου Εκλεκτός 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1318",
      "name": "Knorr Ζωμός Κότας 12 κυβ 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "1319",
      "name": "Aim Οδοντόβ Μέτρια Antiplaque",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "6db091264f494c86b9cf22a562593c82"
    },
    {
      "id": "1320",
      "name": "Proderm Υγρό Απορ/κο 17μεζ 1250ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "991276688c8c4a91b5524b1115122ec1"
    },
    {
      "id": "1321",
      "name": "Klinex Καθ Πατώματος Λεμόνι 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1322",
      "name": "Dove Αφροντούς Deep Nour 500ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1323",
      "name": "Hellmann's Κέτσαπ 560γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "1324",
      "name": "Maggi Πουρές Χ Γλουτ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1325",
      "name": "Νουνού Γάλα Εβαπορέ 170γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1326",
      "name": "Νουνού Γάλα Ζαχαρούχο 397γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1327",
      "name": "Νουνού Γάλα Εβαπορέ Light 170γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1328",
      "name": "Νουνού Γάλα Εβαπορέ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1329",
      "name": "Νουνού Γάλα Εβαπορέ Light 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1330",
      "name": "Νουνού Frisogrow Γάλα 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "1331",
      "name": "Νουνού Γάλα Σκόνη Frisolac 1ης Βρεφ Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "1332",
      "name": "Νουνού Γάλα Σκόνη Frisomel 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "1333",
      "name": "Νουνού Γάλα Συμπ Μερίδες Διχ 10Χ15γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1334",
      "name": "Νουνού Γάλα Light Μερίδες Διχ 10Χ15γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1335",
      "name": "Cif Λεμόνι Creαm 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1336",
      "name": "Cif Άσπρο Creαm 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1337",
      "name": "Axe Αποσμ Σπρέυ Dark Temptation 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "1338",
      "name": "Klinex Σπρέυ 4σε1 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1339",
      "name": "Hellmann's Μαγιονέζα 225ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "1340",
      "name": "Hellmann's Μαγιονέζα 450ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "1341",
      "name": "Becel Μαργαρίνη Light 40% Λιπ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1342",
      "name": "Ajax Antistatic Καθαριστικό Για Τζάμια Αντλία 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1343",
      "name": "Ajax Τζαμ Crystal Clean Αντ/Κο 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1344",
      "name": "Palmolive Αφρόλ Natural Αμυγδ 650ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1345",
      "name": "Leerdammer Τυρί Τοστ Special 125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1346",
      "name": "Knorr Ζωμός Κότας Σπιτικός 112γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "1347",
      "name": "Knorr Ζωμός Σπιτικός Φρεσκ Λαχανικ 4Χ28γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "1348",
      "name": "Red Bull Ενεργειακό Ποτό 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1349",
      "name": "Johnson's Baby Αφρόλουτρο Μπλε 750ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "1350",
      "name": "Nivea Γαλάκτωμα Καθαρισμού 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "1351",
      "name": "Coca Cola 2Χ1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1352",
      "name": "Calgon Αποσκ/Κο Νερού Σκόνη 950γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1353",
      "name": "Tena Lady Extra 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "0bf072374a8e4c40b915e4972990a417"
    }
  ]
    '''

    product_data = json.loads(json_data)
    save_product_images(product_data)

if __name__ == "__main__":
    main()
