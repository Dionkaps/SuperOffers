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
      "name": "Μύλοι Αγίου Γεωργίου Easy Bake Μειγ Muffin 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "1",
      "name": "Γιώτης Φρουιζελέ Φράουλα 2X100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "2",
      "name": "Γιώτης Κρέμα Ζαχαροπλ Βανίλια 117γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "3",
      "name": "Γιώτης Κρέμα Παιδικη Φαρίν Λακτέ Μπισκότο 300γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "4",
      "name": "Άλτις Παραδοσιακό Ελαιόλαδο Παρθένο 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "5",
      "name": "Μεβγάλ Κεφίρ 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "6",
      "name": "Χρυσή Ζύμη Λουκανικοπιτάκια Κατεψυγμένα Κουρού 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "7",
      "name": "Syoss Hairspray Max Ultra Strong 400ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "8",
      "name": "Kellogg's Coco Pops Chocos 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "9",
      "name": "Soupline Mistral Μαλακτικό Συμπ 28πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "10",
      "name": "Nestle Nesquik 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "11",
      "name": "Amita Motion Φυσικός Χυμός 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "12",
      "name": "Σπάλα Βόειου Α/Ο Νωπή Ελλ Εκτρ Άνω Των 5 Μην",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "13",
      "name": "Δέλτα Advance Επιδορπιο Λευκό 2χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "14",
      "name": "Cesar Clasicos Σκυλ/Φή Μοσχ 150γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "15",
      "name": "Κιλότο Βόειου Α/Ο Νωπό Ελλ Εκτρ Άνω Των 5 Μην",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "16",
      "name": "Γιώτης Κουβερτούρα Γαλακ Σταγ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "17",
      "name": "Klinex Χλωρίνη Lemon 2λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "18",
      "name": "Μινέρβα Αραβοσιτέλαιο 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "19",
      "name": "Nan Optipro 4 Γάλα Σε Σκόνη Δεύτερης Βρεφικής Ηλικίας 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "22",
      "name": "Όλυμπος Γάλα Ζωής Πλήρες Υψ Παστ 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "23",
      "name": "Pampers Πάνες Premium Care Νο 2 4-8κιλ 23τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "24",
      "name": "Omo Σκόνη 425γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "25",
      "name": "Κατσίκια Νωπά Ελλην Γαλ Τεμ Χ/Κ Χ/Σ  Συσκ/Νο",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d3385ff161f0423aa364017d4413fa77"
    },
    {
      "id": "26",
      "name": "Nivea Κρέμα 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "27",
      "name": "Γιώτης Κρέμα Παιδική Φαρίν Λακτέ 300γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "28",
      "name": "Kerrygold Τυρί Regato Τριμ.400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "29",
      "name": "Klinex Χλωρίνη Ultra Lemon 1250ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "30",
      "name": "Φάγε Τρικαλινό Τυρί Ζαρί Light Φάγε 380γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "31",
      "name": "Παπαδοπούλου Πτι Μπερ Ολικ Αλ 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "35cce434592f489a9ed37596951992b3"
    },
    {
      "id": "32",
      "name": "Φάγε Γιαούρτι Αγελαδίτσα 4% 3χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "33",
      "name": "Μέλισσα Τορτελίνια Γεμ Τυρίων 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "34",
      "name": "Gordon's Τζιν 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "35",
      "name": "Φάγε Total Γιαούρτι 2% 3x200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "36",
      "name": "Μεβγάλ Φέτα Vacuum 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "37",
      "name": "Dirollo Τυρί Cottage 2,2% Λιπ 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "39",
      "name": "Νίκας Γαλοπούλα Καπνιστή Φέτες 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "40",
      "name": "Elvive Color Vive Γαλακτ Μαλ 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "41",
      "name": "7 Days Κρουασάν Κακάο 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "42",
      "name": "Bref Power Active Wc Block Ωκεαν 50γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "43",
      "name": "Pampers Prem Care No4 8-14κιλ 34τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "44",
      "name": "CIF Spray Κουζίνας 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "45",
      "name": "Brasso Γυαλιστικό Μετάλλων 150ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "46",
      "name": "Everyday Σερβ Maxi Nig/Ultra Plus Sens 18τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "47",
      "name": "Νουνού Frisogrow Γάλα 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "48",
      "name": "Μπούτι Χοιρινό Α/Ο Νωπό Ελλ Χ/Δ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "49",
      "name": "Skip Υγρό Πλ Παν/Μικρ 26πλ 910ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "50",
      "name": "Cif Άσπρο Creαm 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "51",
      "name": "Μπανάνες Chiquita Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "52",
      "name": "Agrino Φακές Ψιλές Εισαγωγής 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "53",
      "name": "Το Μάννα Παξιμάδια Λαδ Κυθήρων 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "54",
      "name": "Almiron-3 Γάλα Σε Σκόνη Τρίτης Βρεφικής Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "55",
      "name": "Tuboflo Αποφρακτικό Σκόνη Φάκελ 100g",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "56",
      "name": "Sprite 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "57",
      "name": "Pampers Πάνες Μωρού 31τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "58",
      "name": "Όλυμπος Γιαούρτι Στραγγ 10% Λ 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "59",
      "name": "Hellmann's Σαλάτα Φάρμα Κηπ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4f205aaec31746b89f40f4d5d845b13e"
    },
    {
      "id": "60",
      "name": "Neomat Υγρό Απορρυπαντικό Ρούχων Τριαντάφυλλο 62μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "61",
      "name": "Gelita Ζελατίνη Φύλλα 20γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "62",
      "name": "Barilla Μακαρόνια Ν5 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "63",
      "name": "Nescafe Azera Καφές Espresso 100% Arabica 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "65",
      "name": "Elnett Λακ Βαμμένα Μαλλ Satin 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "66",
      "name": "Maggi Noodles Γεύση Κοτόπουλο 60γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eef696c0f874603a59aed909e1b4ce2"
    },
    {
      "id": "67",
      "name": "OralB Χειρ Οδοντoβ 1/2/3 Clas Care 40 Med 2 τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "6db091264f494c86b9cf22a562593c82"
    },
    {
      "id": "68",
      "name": "Φάγε Γιαούρτι Αγελάδος 2% Λ 3X200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "69",
      "name": "7 Days Κρουασάν Mini Κακάο 107γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "70",
      "name": "Ferrero Kinder Σοκολ 2πλη 16τεμ Χ Γλουτ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "71",
      "name": "Purina Gold Gourmet Γατ/Φή Μους Ψάρι 85γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "72",
      "name": "Knorr Ζωμός Κότας Σπιτικός 112γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "73",
      "name": "Pummaro Χυμός Τομάτα 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "74",
      "name": "Babylino Sensitive No6 Econ 15-30κιλ 40τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "75",
      "name": "Friskies Γατ/Φή Πατέ Μοσχάρι 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "76",
      "name": "Δέλτα Φυσικ Χυμός Smart Ροδ Βερ200ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "77",
      "name": "Εύρηκα Σκόνη Antikalk 54γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "78",
      "name": "Dove Σαπούνι 100γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "79",
      "name": "Υφαντής Ζαμπόν Μπούτι Βραστό Σε Φέτες 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "80",
      "name": "Airwick Αντ/Κο Αποσμ Χώρου Βαν/Ορχιδ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "21051788a9ff4d5d9869d526182b9a5f"
    },
    {
      "id": "82",
      "name": "Δέλτα Advance Επιδ Μπαν/Μηλο 2Χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "83",
      "name": "Κρι Κρι Γιαούρτι Στραγγιστό 2% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "84",
      "name": "Βεμ Ρώσικη Σαλάτα 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4f205aaec31746b89f40f4d5d845b13e"
    },
    {
      "id": "85",
      "name": "Καλλιμάνης Πέρκα Φιλέτο 595γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "86",
      "name": "Coca Cola 6Χ330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "87",
      "name": "Κύκνος Τοματά Τριμμενη 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "88",
      "name": "Tsakiris Πατατάκια Αλάτι 72γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "89",
      "name": "Κύκνος Τομάτα Ψιλ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "90",
      "name": "Ava Υγρό Πιάτων Ξύδι/Μήλο/Μέντα 430ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "91",
      "name": "Πορτοκ Μερλίν - Λανε Λειτ- Ναβελ Λειτ Κατ Α Εγχ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "93",
      "name": "Fissan Baby Ενυδατική κρέμα 150 ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "94",
      "name": "Anatoli Πιπέρι Μαύρο Μύλος 45gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "96",
      "name": "Twix Σοκολάτα Μπισκότο 50γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "97",
      "name": "Μήλα Στάρκιν Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "98",
      "name": "Pedigree Σκυλ/Φή Πατέ Κοτοπ/Μοσχ 300γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "99",
      "name": "Nestle Fitness Μπαρες Δημητριακών Crunchy Caramel 6X23.5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "100",
      "name": "Πορτοκ Βαλέντσια  Κατ Α Εγχ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "101",
      "name": "Kellogg's Special Κ 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "102",
      "name": "Pedigree Denta Stix Med Σκύλου 180γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "103",
      "name": "Χρυσή Ζύμη Τυροπιτάκια 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "105",
      "name": "Lenor Μαλακτικό Gold Orchid 26πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "106",
      "name": "Fego Καμφορά Πλακέτα 6τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "8f98818a7a55419fb42ef1d673f0bb64"
    },
    {
      "id": "107",
      "name": "Όλυμπος Ταχίνι Χ Γλουτ 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "108",
      "name": "Ballantines Ουίσκι 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "109",
      "name": "Heineken Μπύρα Premium Lager 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "111",
      "name": "Zewa Deluxe Χαρτί Υγείας 3 Φύλλα 8τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "112",
      "name": "Κάλας Αλάτι Θαλασσινό Κλασικό 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "113",
      "name": "Knorr Κυβοι Λαχανικών 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "114",
      "name": "Μεβγάλ Τριμμένο Σκληρό Τυρί 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "115",
      "name": "Τράτα Τόνος Φιλέτο 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "116",
      "name": "Σουρωτή Ανθρακούχο Φυσικό Νερό 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "117",
      "name": "Everyday Σερβ/Κια XL All Cotton 24τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "118",
      "name": "Pyrox Εντομ/Ko Σπιράλ 20τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "8f98818a7a55419fb42ef1d673f0bb64"
    },
    {
      "id": "119",
      "name": "Babylino Sensitive No1 2-5κιλ 28τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "120",
      "name": "Χρυσή Ζύμη Μπουγάτσα Θεσσαλονίκης Με Πραλίνα 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "121",
      "name": "Nescafe Cappuccino 10φακ 140γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "122",
      "name": "Agrino Ρύζι Φανσύ Για Γεμιστά Χ Γλουτ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "123",
      "name": "Καλλιμάνης Γαρίδες Αποφλ Μικρές 425γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "124",
      "name": "Υφαντής Λουκάνικα Βιέννα Αποφλ Χ Γλουτ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "125",
      "name": "Fissan Baby Σαπούνι 90γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "128",
      "name": "Μήλα Στάρκιν Χύμα",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "129",
      "name": "Agrino Ρύζι Bella Parboiled Χ Γλουτ 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "130",
      "name": "St Clemens Μπλέ Τυρί Δανίας 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "131",
      "name": "Iglo Fish Sticks 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "132",
      "name": "Μελιτζάνες Φλάσκες Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "133",
      "name": "Νίκας Λουκάν Φρανκ Γαλοπ Χ Γλ 280γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "134",
      "name": "Pummaro Κέτσαπ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "135",
      "name": "Palette Λακ Πολύ Δυνατή 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "136",
      "name": "Ελιά Νεαρού Μοσχ Α/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "137",
      "name": "3 Άλφα Φασόλια Μέτρια 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "138",
      "name": "Knorr Κύβοι Ζωμού Λαχανικών 12λιτ 24τεμάχια",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "139",
      "name": "Lux Σαπούνι Soft/Creamy 125γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "140",
      "name": "Νουνού Γάλα Σκόνη Frisomel 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "141",
      "name": "Υφαντής Πίτσα Rock N Roll 3Χ460γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3f38edda7854447a837956d64a2530fa"
    },
    {
      "id": "142",
      "name": "Tena Lady Maxi 12τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "143",
      "name": "Μέλισσα Σπαγγέτι Ν6 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "144",
      "name": "Pescanova Μύδια Ψίχα 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "145",
      "name": "Όλυμπος Γιαούρτι Στραγγιστό 2% Λιπ 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "146",
      "name": "Calgon Αποσκ/Κο Νερού Σκόνη 950γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "147",
      "name": "Ferrero Kinder Bueno Σοκ/Τα 43γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "148",
      "name": "Creta Farm Λουκάνικα Τρικάλων Με Πράσο 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "149",
      "name": "Donna Οινόπνευμα Καθαρό 245ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "150",
      "name": "Pampers Active Baby No5 11-16κιλ 51τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "152",
      "name": "Colgate Οδ/Μα Total Original 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "153",
      "name": "Μπούτι Χοιρινό Α/Ο Νωπό Εισ Χ/Δ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "154",
      "name": "Wella Flex Σπρέυ Ultra Strong 250ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "155",
      "name": "Φάγε Τυρί Τριμμένο Gouda 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "156",
      "name": "Νουνού Κρέμα Γάλακτος Πλήρης 330ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4e4cf5616e0f43aaa985c1300dc7109e"
    },
    {
      "id": "157",
      "name": "Nescafe Classic Στιγμιαίος Καφές 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "158",
      "name": "Aim Οδ/Μα Παιδ 2/6ετων 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "159",
      "name": "Ροδάκινα Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "160",
      "name": "Scotch Brite Σφουγγαράκι Πράσ Κλασ 1τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "161",
      "name": "Dettol Κρεμοσάπουνο Soothe 250ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "162",
      "name": "Libero Swimpants Πάνες Midi 10-16κιλ 6τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "163",
      "name": "Amstel Μπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "164",
      "name": "Libresse Σερβιέτες Ultra Thin Long Wings 8τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "165",
      "name": "Βιτάμ Μαργαρίνη Soft Light 39% Λιπ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "166",
      "name": "Πέρκα Φιλέτο Κτψ Εισ Συσκ/Νη",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "167",
      "name": "Sprite Αναψυκτικό 1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "168",
      "name": "Crunch Σοκολάτα Γάλακτος 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "169",
      "name": "Barilla Σάλτσα Pesto Alla Genovese 190γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "170",
      "name": "Afroso Wc Block Τριαντ 2Χ40ΓΡ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "171",
      "name": "Όλυμπος Γάλα Κατσικίσιο Hπ 3,5% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "172",
      "name": "Libresse Σερβ Goodnight Clip 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "173",
      "name": "Παυλίδης Μέρεντα Με Φουντούκι 570γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "174",
      "name": "Tena Lady Extra 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "0bf072374a8e4c40b915e4972990a417"
    },
    {
      "id": "175",
      "name": "Ροδόπη Γάλα Χ Λακτόζη 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "176",
      "name": "Palmolive Κρεμ Μέλι Γάλα Αντ/κο 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "178",
      "name": "Barilla Πένες Rigate Νο 73 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "179",
      "name": "Μεβγάλ Στραγγιστό Γιαούρτι 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "180",
      "name": "Καραμολέγκος Ψωμί Τοστ Σταρένιο 680γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "181",
      "name": "Βιτάμ Soft Μαργαρίνη 3/4 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "182",
      "name": "Cif Λεμόνι Creαm 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "183",
      "name": "Omo Σκόνη Πλυντ Τροπ Λουλούδια 45πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "184",
      "name": "Παπαδοπούλου Caprice Ν6 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "35cce434592f489a9ed37596951992b3"
    },
    {
      "id": "185",
      "name": "Νουνού Ρόφημα Γάλακτος Calciplus 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "186",
      "name": "Όλυμπος Γάλα Επιλεγμ 3,7% Λ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "187",
      "name": "Καλλιμάνης Γλώσσα Φιλέτο 595γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "188",
      "name": "Sanitas Μεμβράνη Διάφανη 30μετ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "189",
      "name": "Alfa Πίτσα Μαργαρίτα Κατεψυγμένη 730γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3f38edda7854447a837956d64a2530fa"
    },
    {
      "id": "190",
      "name": "Μήλα Στάρκιν Ζαγορ Πηλίου ΠΟΠ Κατ Έξτρα",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "191",
      "name": "Asti Martini Αφρώδης Οίνος 0,75λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "192",
      "name": "Pampers Πάνες Premium Care Nο 3 5-9 κιλ 20τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "193",
      "name": "Klinex Σκόνη Πλυντηρίου Ρούχων Original 44μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "194",
      "name": "Zewa Χαρτι Κουζίνας Wisch And Weg Economy 3τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "195",
      "name": "Nivea Νερό Διφασ Ντεμακ Ματιών 125ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "196",
      "name": "OralB Οδ/Μα Pro Exp Prof Prot 75m",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "197",
      "name": "Nestle Cookie Crispies 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "198",
      "name": "Nescafe Dolce Gusto Cappuccino 16 Καψ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "199",
      "name": "Skip Υγρό Απορρυπαντικό Ρούχων Spring Fresh 42μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "201",
      "name": "Ferrero Kinder Delice Κέικ 39γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "202",
      "name": "Klinex Υγρό Απορρυπαντικό Ρούχων Fresh Clean 40μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "203",
      "name": "Zewa Χαρτί Υγείας Deluxe Χαμομήλι 3 Φύλλα 8τεμ 768γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "204",
      "name": "Cair Αφρώδης Λευκός Ημίξηρος Οίνος 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "205",
      "name": "Τρικαλινό Τυρί Φάγε Ελαφ.Φετ.200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "206",
      "name": "Dove Κρεμοσ/νο Ανταλ Regul 500ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "207",
      "name": "Ίον Κακάο 125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "208",
      "name": "Babylino Πάνες Μωρού Sensitive 9-20 κιλ Nο 4+ 19τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "209",
      "name": "Tsakiris Πατατάκια Ρίγανη 72γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "210",
      "name": "Νουνού Γάλα Ζαχαρούχο 397γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "211",
      "name": "Καρπούζια Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "212",
      "name": "Friskies Active Σκυλ/Φή Ξηρά Vital 1,5κιλ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "214",
      "name": "Το Μάννα Παξιμάδι Κρίθινο 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "215",
      "name": "Χρυσά Αυγά Εξαίρετα Φρέσκα Large 6τ Χ 63γρ Πλαστ Θήκη",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d2babbc7355444ca0d27633207e4743"
    },
    {
      "id": "216",
      "name": "Klinex Χλωρίνη Classic 2λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "217",
      "name": "Μπριζόλες Καρέ/Κόντρα Χοιρ Νωπές Εισ Μ/Ο ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "218",
      "name": "Μεβγάλ Παραδοσιακό Γιαούρτι Κατσικ 220γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "219",
      "name": "Μύλοι Αγίου Γεωργίου Καλαμποκάλευρο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "220",
      "name": "Agrino Φασόλια Μέτρια 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "221",
      "name": "Μελιτζάνες Φλάσκες Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "222",
      "name": "Babylino Πάνες Μωρού Sensitive No 5+ Εως 27 κιλ 16τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "223",
      "name": "Bonne Maman Μαρμελάδα Φρα Χ Γλ.370γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "224",
      "name": "Γιώτης Μαγιά 3φακ 8γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "225",
      "name": "Pampers Πάνες Μωρού Premium Pants Nο 4 9-15κιλ 38τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "226",
      "name": "Μεβγάλ Μανούρι 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "227",
      "name": "Nestle Fitness Bars Σοκολάτα 6Χ23,5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "228",
      "name": "Becel Μαργαρίνη Light 40% Λιπ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "229",
      "name": "Elvive Extraordinary Oil Universal 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "230",
      "name": "Παπαδοπούλου Κριτσίνια Σουσάμι 130γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "231",
      "name": "Maltesers Κουφετάκια Σοκολ 37gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "232",
      "name": "Pantene Σαμπουάν Αναδόμησης 360ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "233",
      "name": "Snickers Σοκολάτα 50γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "234",
      "name": "Μεβγάλ Harmony 1% Λεμ 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "235",
      "name": "Κορπή Φυσικό Μεταλλικό Νερό 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "236",
      "name": "Champion Κρουασ Πραλίνα Φουντουκ 4X70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "237",
      "name": "Κριθαράκι Μίσκο Χονδρό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "238",
      "name": "Becel Pro Activ Ρόφημα Με Γαλ 1,8% Λ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "239",
      "name": "Heineken Μπύρα 6X330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "241",
      "name": "Κρίς Κρίς Τόστιμο Ψωμί Τόστ Σταρένιο 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "242",
      "name": "Αγγούρια Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "243",
      "name": "Babylino Πάνες Μωρού Sensitive 11 - 25κιλ No 5 18τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "244",
      "name": "Agrino Ρύζι Σουπέ Γλασέ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "245",
      "name": "Pampers Prem Care No5 11-18κιλ 30τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "246",
      "name": "Agrino Ρύζι Φάνσυ Ελλάδας 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "247",
      "name": "Λάβδας Καραμέλες Βούτυρου 0% Ζαχαρ 32γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7cfe21f0f1944b379f0fead1c8702099"
    },
    {
      "id": "248",
      "name": "Παυλίδης Σοκολατα Υγειας Πορτοκ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "249",
      "name": "Philadelphia Τυρί 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "250",
      "name": "Quaker Νιφ Βρώμης Ολ Άλεσης 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "251",
      "name": "Όλυμπος Γάλα Freelact 1λιτ Χ.Λακτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "252",
      "name": "Μάσκα Προσ 10τεμ 1 Χρήση",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "253",
      "name": "Τσιλιλή Τσίπουρο Χ Γλυκάνισο 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "254",
      "name": "Πλωμάρι Ούζο 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "255",
      "name": "Melissa Σιμιγδάλι Χονδρό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "256",
      "name": "Χρυσά Αυγά Φρέσκα Medium 53/63 γρ.τεμ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d2babbc7355444ca0d27633207e4743"
    },
    {
      "id": "257",
      "name": "Άριστον Αλάτι Ιμαλαΐων Φιάλη 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "258",
      "name": "Καλλιμάνης Καλαμαράκι Κομ Καθαρ 595γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "259",
      "name": "Εβόλ Γάλα Παστερ Αγελαδ Βιολ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "261",
      "name": "Dove Αποσμ Σπρέυ 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "262",
      "name": "McCain Πατάτες Mediterannean 750γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5c5e625b739b4f19a117198efae8df21"
    },
    {
      "id": "263",
      "name": "Canderel Υποκατάστατο Ζάχαρης 120 Δισκία",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a885d8cd1057442c9092af37e79bf7a7"
    },
    {
      "id": "264",
      "name": "Hellmann's Μαγιονέζα 225ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "265",
      "name": "Νουνού Γάλα Εβαπορέ 170γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "267",
      "name": "Coca Cola 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "268",
      "name": "Chupa Chups Melody Γλυφιτζ 12γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7cfe21f0f1944b379f0fead1c8702099"
    },
    {
      "id": "271",
      "name": "Life Φρουτοποτό Πορτ/Μηλ/Καρ 400ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "272",
      "name": "Frulite Φρουτοπ Καροτ/Πορτ/Μαγκ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "273",
      "name": "Quaker Τραγ Μπουκ 4 Ξηροί Καρποί 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "274",
      "name": "Μεβγάλ Γάλα Αγελ Λευκό Πλήρες 3,5% 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "275",
      "name": "Alfa Μπουγάτσα Με Σπανάκι Και Τυρί Κατεψυγμένη 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "276",
      "name": "Μεβγάλ Ζελέ Φράουλα 3Χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "277",
      "name": "Ελιά Βόειου Α/Ο Νωπή Ελλ Εκτρ Άνω Των 5 Μην ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "278",
      "name": "Μπάρμπα Στάθης Σπανάκι Φύλλα 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "279",
      "name": "Jumbo Σνακ Γαριδάρες 85gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "f87bed0b4b8e44c3b532f2c03197aff9"
    },
    {
      "id": "280",
      "name": "Everyday Σερβ Maxi Nig/Ultra Plus Hyp 18τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "281",
      "name": "Παπουτσάνη Σαπούνι Πρασ Παραδ 125γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "282",
      "name": "Φλώρα Αραβοσιτέλαιο 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "283",
      "name": "Μεβγάλ Ξινόγαλο 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "284",
      "name": "Μπάρμπα Στάθης Αρακάς 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "285",
      "name": "Everyday Σερβ Super/Ultra Plus Sens 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "286",
      "name": "EveryDay Natural Fresh Υγρό Ευαίσθ Περιοχ 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "287",
      "name": "Gillette Fusion Proglide 5+1 Ανταλ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "288",
      "name": "Syoss Cond Βαμμένα Μαλ 500ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "289",
      "name": "Αχλάδια Κρυσταλία Εγχ Εξτρα ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "291",
      "name": "Duck Στερεό Block Aqua Blue 40ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "292",
      "name": "Klinex Καθαριστικό Τουαλέτας Block Ροζ Μανόλια 55γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "293",
      "name": "Ζαγόρι Νερό Athletic 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "294",
      "name": "Septona Παιδικό Αφρόλουτρο & Σαμπουάν Αγορια 750ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "295",
      "name": "Μήλα Στάρκιν Κατ Έξτρα Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "296",
      "name": "3 Άλφα Φασόλια Γίγαντες Εισαγωγής 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "297",
      "name": "Aim Οδοντόβ Μέτρια Antiplaque",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "6db091264f494c86b9cf22a562593c82"
    },
    {
      "id": "298",
      "name": "Wella Koleston Βαφή Μαλ Ν7/77",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "09f2e090f72c4487bc44e5ba4fcea466"
    },
    {
      "id": "299",
      "name": "Ajax Τζαμιών 450ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "300",
      "name": "Κρασί Της Παρέας Ερυθρό 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "301",
      "name": "La Vache Qui Rit Τυρί Cheddar Φέτες 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "302",
      "name": "Ροδόπη Γιαούρτι Πρόβειο 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "303",
      "name": "Omino Bianco Υγρό Blacκ Wash 25πλ 1,5λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "304",
      "name": "Coca Cola 1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "306",
      "name": "Sanitas Σακ Απορ Ultra 52Χ75cm 10τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "307",
      "name": "Gillette Venus Close&Clean+2 Ανταλ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "308",
      "name": "Ava Υγρό Πιάτων Perle Classic 900ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "309",
      "name": "Dove Deodorant Κρέμα Rollon 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "310",
      "name": "Klinex Υγρά Πανάκια 30τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "311",
      "name": "Noxzema Αποσμ Rollon Classic 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "312",
      "name": "Κιλότο Νεαρού Μοσχ Α/Ο Νωπό Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "313",
      "name": "Sanitas Αντικολλητικό Χαρτί 8μετ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "314",
      "name": "Μεβγάλ Ζελέ Κεράσι 3Χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "315",
      "name": "Ζαναέ Ντολμαδάκια 280γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "316",
      "name": "Hansaplast Φυσική Ελαφρόπετρα",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "a610ce2a98a94ee788ee5f94b4be82c2"
    },
    {
      "id": "317",
      "name": "Trata Σαρδέλα Λαδιού 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "319",
      "name": "Ferrero Kinder Σοκολ Bars Χ Γλουτ 8τ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "320",
      "name": "Johnson Baby Βρεφικό Σαμπουάν Αντλιά 300ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "321",
      "name": "Νουνού Κρέμα Γάλακτος Light 200ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4e4cf5616e0f43aaa985c1300dc7109e"
    },
    {
      "id": "322",
      "name": "Flokos Σκουμπρί Φιλέτο Καπνιστό 160gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "323",
      "name": "Fissan Baby Σαπούνι 30% Eνυδ Kρέμα 100gr",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "324",
      "name": "Μάσκες Προστασ Προσώπου 50τεμ",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "325",
      "name": "Μίνι Ούζο Γλυκάνισο 200ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "326",
      "name": "Πατάτες  Κύπρου  Κατ Α Συσκ/Νες",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "327",
      "name": "Μάσκες Προστασ Προσώπου 50τεμ",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "328",
      "name": "Nestle Nesquik Ρόφημα Σακούλα 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "329",
      "name": "Παλίρροια Ντολμαδάκια Γιαλαντζί 280γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "331",
      "name": "Quanto Μαλακτ Ρουχ Ελλ Νησ 2λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "332",
      "name": "Softex Χαρτοπετσέτες Λευκές 30x30 56τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "333",
      "name": "Molto Κρουασάν Πραλίνα 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "334",
      "name": "Ajax Υγρό Κατά Των Αλάτων Spray Expert 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "335",
      "name": "Παπαδοπούλου Αρτοσκεύασμα Πολύσπορο 540γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "336",
      "name": "Μεταξά 3 Μπράντυ 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "337",
      "name": "Persil Black Essenzia Απορ Υγρ 25πλ 1,5λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "338",
      "name": "Oral B Στοματικό Διαλ Δοντ/Ουλων 500ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "181add033f2d4d95b46844abf619dd30"
    },
    {
      "id": "339",
      "name": "Μεβγάλ Τριμμένο Σκλήρο Τυρί 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "340",
      "name": "Πατάτες  Κύπρου  Κατ Α Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "341",
      "name": "Dixan Gel 30πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "342",
      "name": "Babylino Πάνες Μωρού Sensitive 3-6κιλ Nο 2 26τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "344",
      "name": "Proderm Ενυδατική Κρέμα 150ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "345",
      "name": "Fairy Υγρό Πιάτων Ultra Κανονικό 900ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "346",
      "name": "Elite Φρυγανιά Τρίμμα 180γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "347",
      "name": "Αρκάδι Υγρό Πλυντ Baby Με Σαπούνι 26πλυς",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "991276688c8c4a91b5524b1115122ec1"
    },
    {
      "id": "348",
      "name": "Δέλτα Vitaline 0% Τρ Φρουτ/Δημ 380γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "349",
      "name": "Elite Φρυγανιές Σίκαλης 180γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "350",
      "name": "Ava Υγρό Πιάτων Perle Σύμπλεγμα Βιταμινών 430ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "351",
      "name": "Nivea Γαλάκτωμα Καθαρισμού 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "352",
      "name": "Οίνος Ερ Γλυκ Μαυροδάφνη Αχαΐα 375ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "353",
      "name": "Absolut Βότκα 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "354",
      "name": "Αλλοτινό Οίνος Ερυθρ Ημιγλυκ 0,5ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "355",
      "name": "Bravo Καφές Κλασικός 95γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "357",
      "name": "Johnson's Baby Κρέμα Μαλλ Χωρ Κομπ 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "358",
      "name": "Fa Αφρόλ Yoghurt Van Honey 750m",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "359",
      "name": "Johnson's Baby Λοσιόν Bedtime 300ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "360",
      "name": "Coca Cola 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "361",
      "name": "Χρυσή Ζύμη Σφολιάτα 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "362",
      "name": "Amita Φυσικός Χυμός Πορτοκάλι 100% 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "363",
      "name": "Κανάκι Βάση Πίτσας Κατεψυγμένη 660γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "364",
      "name": "Χρυσή Ζύμη Στριφταρi Τυρί Μυζ Μακεδον 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "365",
      "name": "Finish All In 1 Καψ Πλυντ Πιάτ Max Regular 27τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "366",
      "name": "Klinex Χλωρίνη Classic 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "367",
      "name": "Ήπειρος Τυρί Ελαφρύ Σε Άλμη 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "368",
      "name": "Akis Καλαμποκάλευρο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "369",
      "name": "Head & Shoulders Σαμπουάν Total Care 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "370",
      "name": "Proderm Σαμπουάν/Αφρόλουτρο 1-3 400ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "371",
      "name": "Activel Plus Αντισηπτικό Gel Χεριών 500ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "372",
      "name": "Ferrero Kinder Αυγό Εκπλ Χ Γλουτ 3τ 60γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "373",
      "name": "Γιώτης Φρουτόκρεμα 5 Φρούτα 300γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "374",
      "name": "Γιώτης Super Mousse Κακ 234γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "375",
      "name": "Παπαδοπούλου Φρυγανιές Χωριάτικες Ολικής Άλεσης 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "376",
      "name": "Γιαννιώτη Φύλλο Κρουσ Νωπό 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "377",
      "name": "Ήπειρος Φέτα Μαλακή 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "378",
      "name": "Ροδόπη Γιαούρτι Κατσικίσιο 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "379",
      "name": "Ajax Kloron 2σε1 Λεμόνι 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "380",
      "name": "Κρίς Κρίς Τόστιμο Ψωμί Τόστ Ολικής Άλεσης 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "381",
      "name": "Tsakiris Πατατάκια Αλάτι 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "382",
      "name": "Agrino Ρύζι Λαΐς Καρολίνα 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "383",
      "name": "Κατσέλης Κριτσίνια Μακεδονικά 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "384",
      "name": "Όλυμπος Γάλα Επιλεγμ 1,5% Λ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "385",
      "name": "Κοντοβερός Σολωμός Φιλέτο Chum 595γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "386",
      "name": "Όλυμπος Γάλα Βιολ Υψηλ Παστ 3,7% Λ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "387",
      "name": "Όλυμπος Φυσ Χυμός Μηλ Πορτ Kaρότο 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "388",
      "name": "Χρυσά Αυγά Ελληνικά Βιολ 6τ Medium 348γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d2babbc7355444ca0d27633207e4743"
    },
    {
      "id": "389",
      "name": "Νουνού Κρέμα Γάλακτος Πλήρης 2Χ330ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4e4cf5616e0f43aaa985c1300dc7109e"
    },
    {
      "id": "390",
      "name": "Vanish Oxi Action Ενισχυτικό Πλεύσης 1γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "391",
      "name": "Libero Swimpants Πάνες Small 7-12κιλ 6τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "392",
      "name": "Μεβγάλ Στραγγιστό Γιαούρτι 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "393",
      "name": "Υφαντής Σαλάμι Αέρος Χ Γλουτ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "394",
      "name": "Fanta Πορτοκαλάδα 1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "396",
      "name": "Coca Cola Zero 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "398",
      "name": "Κρεμμύδια Ξανθά Ξερά Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "400",
      "name": "Κοκκινόψαρο  Κτψ Εισ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "401",
      "name": "Dewar's Ουίσκι 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "402",
      "name": "Barilla Cannelloni 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "403",
      "name": "Flora Μαργαρίνη Πλακ 70% Λιπ 25% 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "405",
      "name": "Omo Υγρό Απορ Τροπ Λουλ 30πλ 1,95l",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "406",
      "name": "Alfa Φύλλο Χωριάτικο Κιχι Κτψ 750γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "407",
      "name": "Knorr Κύβοι Ζωμού Λαχανικών Extra Γεύση 147γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "408",
      "name": "Γιώτης Sanilac 1 Γάλα Σε Σκόνη Πρώτης Βρεφικής Ηλικίας 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "409",
      "name": "Philadelphia Τυρί Light 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "410",
      "name": "Coca Cola Light 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "412",
      "name": "Φράουλες Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "413",
      "name": "Παυλίδης Γκοφρέτα Υγείας 34γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "414",
      "name": "Pantene Κρέμα Μαλλ Αναδόμησης 270ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "415",
      "name": "Bailey's Irish Cream Λικέρ 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "416",
      "name": "Barilla Maccheroncini Μακαρόνια Για Παστίτσιο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "417",
      "name": "Skip Duo Καψ Πλυντ Ρούχ Active Clean 578γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "418",
      "name": "Fissan Baby Πούδρα 100gr",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "419",
      "name": "Ajax Καθαριστικό Ultra 7 Φυσ Σαπούνι 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "420",
      "name": "Palette Βαφή Μαλ Ξανθό N8",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "09f2e090f72c4487bc44e5ba4fcea466"
    },
    {
      "id": "422",
      "name": "Axe Αποσμητικό Σπρέυ Africa 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "423",
      "name": "Pummaro Χυμός Τομάτα Κλασικός 3Χ250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "424",
      "name": "Gordons Space Τζιν Original 275ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "425",
      "name": "Pedigree Rodeo Σκυλ/Φή Μοσχ 70γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "426",
      "name": "Frulite Φρουτοπoτό Πορτ/Βερικ 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "427",
      "name": "Δέλτα Milko Γάλα Παστερ 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "428",
      "name": "Χρυσή Ζύμη Κασερόπιτα Σπιτική 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "429",
      "name": "Καραμολέγκος Ψωμί Τοστ Σταρένιο Μίνι 340g",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "430",
      "name": "Όλυμπος Γάλα Ζωής Λευκό Ελαφρύ Παστ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "431",
      "name": "Ajax Antistatic Καθαριστικό Για Τζάμια Αντλία 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "432",
      "name": "Κρεμμύδια Κόκκινα Ξερά Εισ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "433",
      "name": "Skip Υγρό Regular 30πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "434",
      "name": "Δέλτα Ρόφημα Advance Υψ Παστ Μπουκ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "435",
      "name": "Dixan Σκόνη Πλυντ 42πλ 2,31γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "436",
      "name": "Philadelphia Τυρί 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "437",
      "name": "Life Φρουτοπ Κρανμπ/Ρασμπ/Μπλουμπ 1lt",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "438",
      "name": "Creta Farms Εν Ελλάδi Λουκάν Παραδ Χ Γλουτ 340γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "439",
      "name": "Joya Ρόφημα Σογιας Bio Χ Ζαχ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "440",
      "name": "EggPro Ροφ Πρωτεΐνης Φράουλα Χ Γλουτ 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "441",
      "name": "Wella New Wave Πηλός Γλυπτικής 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "442",
      "name": "Pyrox Εντομ/Κο Σπιράλ 10τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "8f98818a7a55419fb42ef1d673f0bb64"
    },
    {
      "id": "443",
      "name": "Johnnie Walker Ουίσκι Black Label 12ετών",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "444",
      "name": "Μαλαματίνα Ρετσίνα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "445",
      "name": "O.B. Ταμπόν Original Normal 16τμχ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "446",
      "name": "Ace Gentile Ενισχυτικό Πλύσης 2lt",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "448",
      "name": "Χρυσή Ζύμη Πίτσα Μαργαρίτα 2X470γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3f38edda7854447a837956d64a2530fa"
    },
    {
      "id": "449",
      "name": "7 Days Κέικ Bar Κακάο 5Χ30γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "450",
      "name": "Texas Νιφάδες Βρώμης 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "451",
      "name": "Όλυμπος Φυσικός Χυμός Πορτοκάλι 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "452",
      "name": "Alfa Ζύμη Για Πίτσα 600γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "453",
      "name": "Calgon Αποσκληρυντικό Νερού Πλυντηρίου Ρουχων Gel 1.5λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "456",
      "name": "Klinex Advance Απορρυπαντικό Ρούχων Πλυντηρίου Με Χλώριο 2λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "457",
      "name": "Φάγε Total Γιαούρτι Στραγγιστό 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "458",
      "name": "Γιώτης Φρουιζελέ Κεράσι Σε Σκ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "459",
      "name": "3 Άλφα Ρεβύθια Χονδρά Εισαγωγής 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "460",
      "name": "Κοτοπουλα Ολοκληρα Νωπα Τ.65% Πινδος Π.Α.Ελλην Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "461",
      "name": "Μεβγάλ Κρεμα Σοκολάτα 150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "462",
      "name": "Αλλατίνη Κέικ Κακάο Με Κομμάτια Σοκολάτας 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "463",
      "name": "Τοματίνια Βελανίδι Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "464",
      "name": "Πορτοκ Βαλέντσια Εγ Χυμ Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "465",
      "name": "Δέλτα Γάλα Daily Υψ Παστ Χ Λακτ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "466",
      "name": "Δέλτα Milko Κακάο 450ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "467",
      "name": "Flokos Καλαμάρια Φυσ Χυμού 370γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "468",
      "name": "Lurpak Βούτυρο Ανάλατο 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "470",
      "name": "Παυλίδης Kiss Σοκολάτα Γάλ Φράουλα 27,5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "471",
      "name": "Μεβγάλ Τυρί Ημισκλ Μακεδ 420γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "472",
      "name": "Παυλίδης Σοκολάτα Υγείας Ν11 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "473",
      "name": "Persil Express Σκόνη Χεριού 420γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "474",
      "name": "Παπαδοπούλου Μπισκότα Μιράντα Ν16 250γρ 12τεμ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "35cce434592f489a9ed37596951992b3"
    },
    {
      "id": "475",
      "name": "7 Days Κρουασάν Κακάο 3Χ70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "476",
      "name": "Μεβγάλ Only Lact Free 1,5% 1λτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "478",
      "name": "Φάγε Total Γιαούρτι 5% Φάγε 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "479",
      "name": "Omo Bianco Υγρό Αφρ Μασ Παραδοσ 30πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "480",
      "name": "Fornet Καθαρ Φούρνου 300ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "481",
      "name": "Μεβγάλ Ανθότυρο Τυποπ 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "482",
      "name": "Babylino Sensitive Econ Ν5+ 13-27κιλ 42τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "484",
      "name": "Μπάρμπα Στάθης Ρύζι Με Καλαμπόκι 600γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "485",
      "name": "Neomat Σκόνη Πλυντηρίου Ρούχων Άγριο Τριαντάφυλλο 45μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "486",
      "name": "Roli Καθαριστικό Σκόνη Για Όλες Τις Επιφάνειες Λεμονί 500γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "487",
      "name": "Melissa Σιμιγδάλι Ψιλό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "488",
      "name": "Υφαντής Παριζάκι 330γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "489",
      "name": "Folie Κρουασάν Κρέμα Κακαο 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "490",
      "name": "Life Φρουτοποτό Πορτοκ/Μηλ/Καροτ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "491",
      "name": "Amstel Μπύρα 6Χ330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "492",
      "name": "Everyday Σερβ Maxi Nig/Ultra Plus Sens 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "493",
      "name": "Zwan Luncheon Meat 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "494",
      "name": "Softex Χαρτί Υγείας Super Giga 2 Φύλλα 12τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "495",
      "name": "Knorr Κύβοι Ζωμού Κότας 6λιτ 12τεμάχια",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "496",
      "name": "Hellmann's Μουστάρδα Απαλή 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "497",
      "name": "Gillette Αφρός Ξυρ Sens Classic 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "498",
      "name": "Μετέωρα Ξύδι Λευκού Κρασιού 400ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "499",
      "name": "Babylino Πάνες Μωρού Sensitive 4 - 9 κιλ No 3 22τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "500",
      "name": "Babylino Sensitive No5 Econ 11-25κιλ 44τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "501",
      "name": "Μίνι Ούζο Επομ 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "502",
      "name": "Coca Cola 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "503",
      "name": "Camel Υγρο Δερμα Παπουτσιών Μαύρο 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "a610ce2a98a94ee788ee5f94b4be82c2"
    },
    {
      "id": "504",
      "name": "Noxzema Αφρόλ Talc 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "505",
      "name": "Calgon Gel 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "506",
      "name": "Halls Καραμ Cool Menthol 28γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7cfe21f0f1944b379f0fead1c8702099"
    },
    {
      "id": "507",
      "name": "Vanish Oxi Action Ενισχ Πλύσης 500γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "508",
      "name": "Grants Ουίσκι 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "510",
      "name": "Ruffles Barbeque 130γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "511",
      "name": "Gillette Sensor Excel Ανταλ Ξυρ 5 τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "512",
      "name": "Λάπα Νεαρού Μοσχ Α/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "514",
      "name": "Λουξ Λεμονάδα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "516",
      "name": "3 Άλφα Ρύζι Γλασσέ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "518",
      "name": "Δωδώνη Γιαούρτι Στραγγιστό 8% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "519",
      "name": "Χυμός Ρόδι/Μηλ/Καρ Χριστοδούλου 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "520",
      "name": "Έψα Λεμοναδα 232ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "521",
      "name": "Ήλιος Πιπέρι Μαύρο Τριμμένο 40gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "522",
      "name": "Topine Υγρό Επιφ Red Pine 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "523",
      "name": "Calgon Ταμπλέτες 15τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "524",
      "name": "Flora Maργαρίνη Soft 60% Λιπ 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "526",
      "name": "Lux Aφρόλ Magical Beauty 700ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "527",
      "name": "Κρασί Της Παρέας Ροζέ Κοκκινέλι 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "528",
      "name": "Coca Cola Zero 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "529",
      "name": "Vanish Σαμπουάν Χαλιών 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "530",
      "name": "Pescanova Μπακαλιαράκια 600γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "531",
      "name": "Lavazza Καφές Rossa Espresso 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "532",
      "name": "Καρότα Εγχ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "533",
      "name": "Purina One Γατ/Φή Ξηρά Βοδ/Σιτ 800γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "534",
      "name": "Always Σερβ Ultra Platinum Night 6τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "536",
      "name": "Παυλίδης Μερέντα 360γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "537",
      "name": "Gilette Ξυρ Μ/Χ Blue II Slalom 5τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "538",
      "name": "Intermed Reval Plus Gel Χεριών Lollipop 75ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "539",
      "name": "Veet Κρύο Κερι Ταινίες Προσώπου 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "540",
      "name": "Νουνού Gouda Φέτες 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "542",
      "name": "Πορτοκάλια Βαλέντσια Εισ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "543",
      "name": "Ρεπάνη Μοσχοφίλερο Λευκός Οίνος 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "544",
      "name": "Coca Cola Zero 2Χ1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "545",
      "name": "Orzene Condit Μπύρας Κανον Μαλλ 250ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "546",
      "name": "Misko Ταλιατέλλες Σιμιγδ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "547",
      "name": "Autan Family Care Spray 100ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "8f98818a7a55419fb42ef1d673f0bb64"
    },
    {
      "id": "548",
      "name": "Εύρηκα Υγρό Απορρυπαντικό Ρούχων Μασσαλίας 30μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "549",
      "name": "Ribena Φρουτοποτό Φραγκοστάφυλλο 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "550",
      "name": "Ντομάτες Τσαμπί Υδροπ Εγχ  Α",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "551",
      "name": "Παπαδοπούλου Κριτσίνια Μακεδ Ολ Αλ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "552",
      "name": "7 Days Παξιμαδάκια Mini Κλασική Γεύση Bake Rolls 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "553",
      "name": "Glade Αντ/Κο Αποσμ Χώρου Λεβάντα",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "21051788a9ff4d5d9869d526182b9a5f"
    },
    {
      "id": "554",
      "name": "Misko Ολικής Άλεσης Μακαρόνια Σπαγγέτι Ν6 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "555",
      "name": "Hellmann's Μαγιονέζα 450ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "556",
      "name": "Iglo Κροκέτες Ψαριών Κατεψυγμένες 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "557",
      "name": "Lipton Ice Tea Green No Sugar 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "558",
      "name": "Proderm Ενυδατική Κρέμα Sleep Easy 150ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "559",
      "name": "Μάννα Παξιμάδια Κριθαρένιο 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "560",
      "name": "La Vache Qui Rit Τυροβουτιές 4Χ35γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "561",
      "name": "Monster Energy Drink 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "562",
      "name": "Nivea Μάσκα Μέλι για Ξηρ/Ευαίσθ Επιδ 2x7,5ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "563",
      "name": "Νουνού Γάλα Light Μερίδες Διχ 10Χ15γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "564",
      "name": "Gliss Condition Ultimate Color 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "565",
      "name": "McCain Πατάτες Tradition Σακ 1κλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5c5e625b739b4f19a117198efae8df21"
    },
    {
      "id": "566",
      "name": "Υφαντής Παριζακι Γαλοπούλας 330γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "567",
      "name": "Milner Τυρί Φέτες 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "568",
      "name": "Aim Οδ/τσα 2-6 Παιδική",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "6db091264f494c86b9cf22a562593c82"
    },
    {
      "id": "569",
      "name": "Μακεδονικό Ταχίνι Σε Βάζο 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "570",
      "name": "Φάγε Τυρί Flair Cottage 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "571",
      "name": "Τσίπουρα Υδατ Ελλην Α 300/400 Μεσογ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "572",
      "name": "Fytro Σόγια Κιμάς 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "573",
      "name": "Κανάκι Σφολιατ Χωρ Στρ Κουρού 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "574",
      "name": "Rilken Gel Χτεν Clubber 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "575",
      "name": "Κολοκυθάκια Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "576",
      "name": "Nesquik Δημητριακά Extra Choco Waves 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "577",
      "name": "Sani Πάνα Ακρατ Sensitive N4 Xlarge 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "0bf072374a8e4c40b915e4972990a417"
    },
    {
      "id": "578",
      "name": "Ζαγόρι Φυσικό Μεταλλικό Νερό 1.5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "579",
      "name": "Bioten 24η Κρέμα Ενυδ 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "fefa136c714945a3b6bcdcb4ee9e8921"
    },
    {
      "id": "580",
      "name": "Quanto Μαλακτ Μη Συμπ Μπλε 2λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "581",
      "name": "Barilla Λαζάνια Με Αυγά 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "582",
      "name": "Dettol Κρεμοσάπουνο Citrus 250ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "583",
      "name": "Colgate Οδ/τσα Ext Clean Med Twin Pack",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "6db091264f494c86b9cf22a562593c82"
    },
    {
      "id": "584",
      "name": "Τράτα Σαρδέλες Φιλέτο Κατεψυγμένες 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "585",
      "name": "Τεντούρα Κάστρο Λικέρ 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "586",
      "name": "Λουξ Πορτοκαλάδα Ανθρ 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "587",
      "name": "Pescanova Μπακαλιάρος Ρολό Φιλeto 480γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "588",
      "name": "Νίκας Γαλοπ Καπνισ + Gouda Τυρί Light Φετ 280γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "589",
      "name": "Axe Αφροντούς Africa 400ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "590",
      "name": "Ίον Σοκοφρέτα Σοκολ Υγείας 38γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "591",
      "name": "Disaronno Λικέρ 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "592",
      "name": "Κουρτάκη Ρετσίνα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "593",
      "name": "Baby Care Μωρόμαντηλα Sensitive 63τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "92680b33561c4a7e94b7e7a96b5bb153"
    },
    {
      "id": "594",
      "name": "Noxzema Αφρός Ξυρισ Xtr Sens 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "595",
      "name": "Viakal Υγρό Καθαρισμού Κατά Των Αλάτων 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "596",
      "name": "Λουξ Πορτοκαλάδα Μπλε 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "597",
      "name": "Overlay Επίπλων Σπρέυ 250ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "598",
      "name": "Βεργίνα Μπύρα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "599",
      "name": "Johnnie Walker Ουίσκι Κόκκινο 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "600",
      "name": "Παπαδοπούλου Παξιμαδάκια Σίτου 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "601",
      "name": "Λαυράκια Υδατ  Ελλην 400/600 Μεσογ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "602",
      "name": "Libresse Σερβιέτες Invisible Normal 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "603",
      "name": "Misko Μακαρόνια Σπαγγέτι Ν3 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "604",
      "name": "Δέλτα Ρόφημα Advance 80% Λιγ Λακτ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "605",
      "name": "Σολομός Νωπός Φέτα Μ/Δ & Μ/Ο Υδ Νορβ/Εισαγ  Β.Α Ατλ Συσκ/Νοσ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "606",
      "name": "Nestle Cheerios 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "607",
      "name": "Babylino Sensitive No4+ Econ 9-20κιλ 46τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "608",
      "name": "Sani Pants N2 Medium 14τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "0bf072374a8e4c40b915e4972990a417"
    },
    {
      "id": "609",
      "name": "Durex Προφυλακτικά Jeans 12τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "7cfab59a5d9c4f0d855712290fc20c7f"
    },
    {
      "id": "610",
      "name": "Καραμολέγκος Δέκα Αρτοσκεύασμα Σταρένιο Σε Φέτες 550γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "611",
      "name": "Barilla Ζυμαρικά Capellini No1 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "612",
      "name": "Καραμολέγκος Παξαμάς Σικαλης 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "613",
      "name": "Εδέμ Φασόλια Κόκκινα Σε Νερό 240γρ.",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "614",
      "name": "Jannis Παστέλι Σουσάμι Χ Γλ 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "615",
      "name": "Neslac Επιδόρπιο Γάλακτος Βανίλια 4Χ100γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "616",
      "name": "Δέλτα Γιαούρτι Μικ Οικ Φαρμ 2% 2Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "617",
      "name": "Μινέρβα Ελαιόλαδο 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "618",
      "name": "Pillsbury Φυλλο Ζύμης Για Τάρτα 600γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "619",
      "name": "Στήθος Φιλέτο Κοτ Ελλην. Νωπό Ε/Ζ Χύμα ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "620",
      "name": "Johnson Baby Βρεφικό Σαμπουάν Χαμομήλι 300ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "621",
      "name": "Tide Alpine Απορ Χεριού Σκόνη 450γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "622",
      "name": "Hansaplast Universal Αδιάβροχα 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "1b59d5b58fb04816b8f6a74a4866580a"
    },
    {
      "id": "623",
      "name": "Coca Cola Πλαστ 4Χ500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "624",
      "name": "Dettol Αντιβ/κό Σπρέι 500ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "625",
      "name": "Danone Activia Επιδ Γιαουρ Τραγ Απόλ 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "626",
      "name": "Μιμίκος Κοτόπουλο Στηθ Φιλ Νωπό Τυποπ 845γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "463e30b829274933ab7eb8e4b349e2c5"
    },
    {
      "id": "627",
      "name": "Μεβγάλ Topino Απαχο Γάλα Κακάο 450ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "628",
      "name": "Creta Farms Λουκαν Χωριατ Μυρ Χ Γλουτ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "629",
      "name": "Fairy Υγρό Πιάτων Ultra Λεμόνι 900ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "630",
      "name": "Don Simon Kρασί Sangria Χαρτ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "631",
      "name": "Tasty Poppers Classic Ποπ Κορν 81γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8851b315e2f0486180be07facbc3b21f"
    },
    {
      "id": "632",
      "name": "Swiffer Dusters Αντ/κα 10τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "634",
      "name": "Κιλότο Βόειου Α/Ο Νωπό Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "635",
      "name": "Red Bull Ενεργειακό Ποτό 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "636",
      "name": "Coca Cola 2Χ1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "637",
      "name": "Knorr Μανιταρόσουπα 90γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eef696c0f874603a59aed909e1b4ce2"
    },
    {
      "id": "638",
      "name": "Maggi Πουρές Χ Γλουτ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "640",
      "name": "Γιαννιώτη Φύλλο Χωριατ Νωπό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "641",
      "name": "Γιώτης Μπισκοτόκρεμα 300γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "642",
      "name": "Μίσκο Μακαρόνια Ν6 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "643",
      "name": "Πατάτες  Εισ Κατ Α Ε/Ζ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "644",
      "name": "Daκor Corned Beef Μοσχάρι 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "646",
      "name": "Μάσκες Προστ Προσώπου 50τεμ Non-Woven",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "647",
      "name": "Nivea Baby Φυσιολογικός Ορός 24Χ5ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "648",
      "name": "Del Monte Κομπόστα Ανανά Φέτες 565γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "649",
      "name": "Friskies Σκυλ/Φή Βοδ/Κοτ/Λαχ 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "651",
      "name": "Nutricia Biskotti 180γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "652",
      "name": "Μπανάνες Dole Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "653",
      "name": "Ariel Alpine Υγρές Καψ 3σε1 24πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "654",
      "name": "Garnier Νερό Ντεμακιγιάζ Micellaire 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "655",
      "name": "Κύκνος Τοματοπολτός 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5aba290bf919489da5810c6122f0bc9b"
    },
    {
      "id": "656",
      "name": "Μινέρβα Αραβοσιτέλαιο 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "657",
      "name": "Finish Εκθαμβωτικό Υγρο Πλυν Πιάτ 400ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "658",
      "name": "3 Αλφα Ρύζι Καρολίνα 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "659",
      "name": "Meritο Spray Σιδερώματος 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "660",
      "name": "Καραμολέγκος Ψωμί Τόστ Δέκα Χωριάτικο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "661",
      "name": "Ρούσσος Νάμα Κρασί Ερυθρό Γλυκο 375ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "662",
      "name": "Βιτάμ Μαργαρίνη Soft Σκαφ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "663",
      "name": "Kellogg's Corn Flakes 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "664",
      "name": "Soupline Mistral Μαλακτικό 13πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "665",
      "name": "Κανάκι Φύλλο Κρούστας 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "666",
      "name": "Μεβγάλ Γάλα «Κάθε Μέρα» 3.5% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "667",
      "name": "Εύρηκα Bright Ενισχυτικό Πλύσης Πολυκαθαριστικό Λεκέδων 500g",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "668",
      "name": "Υφαντής Μπουκιές Κοτόπουλο Κτψ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "669",
      "name": "Χρυσή Ζύμη Σπιτικά Τριγων Φέτα Κατικ 750γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "670",
      "name": "Palmolive Υγρό Πιάτων Λεμόνι 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "671",
      "name": "Όλυμπος Κεφαλοτύρι Προβ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "672",
      "name": "Zewa Χαρτομάντηλα Soft/Strong 90τμχ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "673",
      "name": "Alfa Κιχι Παραδοσιακή Πίτα Με Τυρί 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "674",
      "name": "Klinex Χλωρίνη Ultra Lemon 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "675",
      "name": "Svelto Gel Υγρό Πιάτων Λεμόνι 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "676",
      "name": "Nutricia Biskotti Ζωάκια 180γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "677",
      "name": "Friskies Adult Ξηρά Γατ/Φή Κουν/Κοτ/Λαχ 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "678",
      "name": "L'Oreal Σαμπ Elvive Color Vive Βαμμένα 400ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "679",
      "name": "Κανάκι Tυροπιτάκια Κουρού 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "680",
      "name": "Λουμίδης Καφές Ελληνικός 490γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "683",
      "name": "Υφαντής Χάμπουργκερ Top Burger 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "684",
      "name": "Σολομός Νωπός Φιλετ/νος Με Δέρμα Υδ Νορβ/Εισαγ  Β.Α Ατλ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "685",
      "name": "Γιώτης Sanilac 2 Γάλα Σε Σκόνη Δεύτερης Βρεφικής Ηλικίας 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "686",
      "name": "Everyday Σερβ Norm/Ultra Plus Hyp 18τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "687",
      "name": "Nivea Κρ Ημέρας Ξηρ/Ευαίσθ Επιδ SPF15 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "688",
      "name": "Δέλτα Γάλα Πλήρες 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "689",
      "name": "Finish Αποσκλ/Κο Αλάτι Πλυν 2,5κιλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "690",
      "name": "Αρνιά Νωπά Ελλην Γαλ Ολοκλ Μ/Κ Μ/Σ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0936072fcb3947f3baf83e31bb5c1cab"
    },
    {
      "id": "691",
      "name": "Φάγε Κεφαλοτύρι Τριμμένο 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "692",
      "name": "Lactacyd Intimate Lotion Ευαίσθ Περιοχ 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "693",
      "name": "Green Cola 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "695",
      "name": "Heineken Μπύρα 4X500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "696",
      "name": "Tuborg Club Σόδα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "698",
      "name": "Lurpak Βούτυρο Αναλ Αλουμ 125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "699",
      "name": "Barilla Μακαρ Linguine Bavette Ν13 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "700",
      "name": "Knorr Ζωμός Κότας Σε Κόκκους Extra Γεύση 88γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "701",
      "name": "Μεβγάλ Ζελέ Ροδάκινο 3Χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "702",
      "name": "Μύλοι Αγίου Γεωργίου Αλεύρι Για Όλες Τις Χρ 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "703",
      "name": "Ajax Uλιτra Υγρό Γενικού Καθαρισμού Λεμόνι 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "704",
      "name": "Mini Babybel Τυρί Classic 10τεμ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "705",
      "name": "Everyday Σερβ Extr Long/Ultra Plus Hyp 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "706",
      "name": "Κανάκι Ζύμη Κατεψυγμένη Κουρού 700γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "707",
      "name": "Δωδώνη Τυρί Φέτα 400γρ Σε Άλμη",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "708",
      "name": "Creta Farms Εν Ελλάδι Κεφτεδάκια Κτψ 420γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "709",
      "name": "Stella Artois Μπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "710",
      "name": "Airwick Αντ/Κο Freshmatic Βαν/Ορχιδ 250ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "21051788a9ff4d5d9869d526182b9a5f"
    },
    {
      "id": "711",
      "name": "Jacobs Καφές Φίλτρου Εκλεκτός 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "712",
      "name": "Lacta Σοκολάτα Γάλακτος 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "713",
      "name": "Μεβγάλ Κεφίρ Lactose Free Με Ροδακ 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "714",
      "name": "Neomat Total Eco Απορ Σκον 14πλ 700γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "715",
      "name": "Frulite Σαγκουίνι/Μανταρίνι 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "716",
      "name": "Nivea Κρ Νύχτας Cellular Anti-Age 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "717",
      "name": "Nestle Ρόφημα Γαλακτ Junior 2+ Rtd 1λιτ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "718",
      "name": "Amita Φρουτοποτό Πορ/Μηλ/Βερ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "719",
      "name": "Μίσκο Κριθαράκι Μέτριο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "720",
      "name": "Κύκνος Κέτσαπ Top Down Χ Γλουτ 580γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "721",
      "name": "Μεβγάλ Harmony Gourmet Πορτοκ Νιφ Σοκ 165γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "722",
      "name": "Μεβγάλ High Protein Vanilla Drink 242ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "723",
      "name": "Amstel Μπύρα 4X500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "724",
      "name": "Ava Υγρό Πιάτων Perle Χαμομήλι/Λεμόνι 1500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "725",
      "name": "Δέλτα Γάλα Ελαφρύ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "726",
      "name": "Babylino Sensitive No3 Econ 4-9κιλ 56τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "727",
      "name": "Dettol Spray Γενικού Καθαρισμού Υγιεινή Και Ασφάλεια Λεμόνι Μέντα 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "728",
      "name": "Airwick Αποσμ Χώρου Stick Up 120γρ 2τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "21051788a9ff4d5d9869d526182b9a5f"
    },
    {
      "id": "729",
      "name": "Μεβγάλ Creme Καραμελέ 150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "730",
      "name": "Τσιλιλή Τσίπουρο Χ Γλυκάνισο 200ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "731",
      "name": "Εβόλ Γιαούρτι Κατσικίσιο Βιολ 190γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "732",
      "name": "Μεβγάλ Τριμμενη Μυζήθρα Ξηρή 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "733",
      "name": "Fairy Υγρό Απορρυπαντικό Πιάτων Power Spray 375ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "734",
      "name": "Biofarma Παστέλι Βιολ Με Σουσάμι 30gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "736",
      "name": "Rio Mare Τόνος Νερόυ 2Χ160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "737",
      "name": "Septona Παιδικό Σαμπουάν Κορίτσια 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "738",
      "name": "Κολοκυθάκια Εγχ Με Ανθό",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "739",
      "name": "Agrino Ρύζι Basmati Χ Γλουτ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "740",
      "name": "Εν Ελλάδι Γαλοπούλα Καπνιστή Φέτες 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "741",
      "name": "Στεργίου Κέικ Ανάμεικτο 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "742",
      "name": "Aim Οδ/μα White System 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "744",
      "name": "Δέλτα Mmmilk Γάλα Οικογεν Χαρτ 1,5% 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "745",
      "name": "Pillsbury Ζύμη Κρουασάν 230γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "747",
      "name": "Zewa Χαρτί Κουζίνας Με Σχέδια 2τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "748",
      "name": "Jose Cuervo Τεκίλα Espec Κιτρ 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "749",
      "name": "Pantene Μάσκα Μαλ Αναδόμησης 2λεπτ 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "750",
      "name": "Pampers Πάνες Μωρού Premium Care Nο 6 13+κιλ 38τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "751",
      "name": "Μάσκα Προσώπου Υφασμ 1τεμ",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "752",
      "name": "Friskies Άμμος Υγιεινής 5κιλ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "753",
      "name": "Σαβόϊ Βούτυρο Τύπου Κερκύρας 250gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "754",
      "name": "Sensodyne Οδ/μα Repair/Protect 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "756",
      "name": "Τσανός Μουστοκούλουρα 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47b5f0016f4f0eb79e3a4b932f7577"
    },
    {
      "id": "757",
      "name": "Fairy Υγρό Πιάτων Ultra Classic 400ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "758",
      "name": "Μεβγάλ Τριμμένο Κεφαλοτύρι 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "759",
      "name": "Όλυμπος Φυσικός Χυμός Πορτ 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "760",
      "name": "Λεμόνια Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "761",
      "name": "Pillsbury Αφρατ Ζυμ Για Πίτσα 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "764",
      "name": "Γιώτης Κρέμα Ζαχαροπλ Μιλφέιγ 170γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "765",
      "name": "Άλφα Μπύρα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "766",
      "name": "Nivea Μάσκα Peel Off 10ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "767",
      "name": "Μήλα Στάρκιν Ψιλά Συσκ/Να ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "768",
      "name": "Ωμέγα Special Ρύζι Νυχάκι 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "769",
      "name": "Πέρκα Φιλέτο Κτψ Εισ Ε/Ζ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "770",
      "name": "Νίκας Ωμοπλάτη Χωρίς Γλουτένη 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "771",
      "name": "Elite Φρυγανιές Σταριού Κουτί 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "772",
      "name": "Γλώσσες Φιλέτο Κτψ Εισ Συσκ/Νες",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "773",
      "name": "Pedigree Σκυλ/Φή Μοσχάρι 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "774",
      "name": "Βίκος Φυσικό Μεταλλικό Νερό 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "775",
      "name": "Γαύρος Νωπός Ελλην Μεσόγ Ολόκλ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c487e038079e407fb1a356599c2aec3e"
    },
    {
      "id": "776",
      "name": "Uncle Bens Ρύζι Basmati 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "777",
      "name": "Εύρηκα Λευκαντικό 60γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "778",
      "name": "Pillsbury Σάλτσα Για Πίτσα 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "779",
      "name": "Swiffer Dusters 5τεμ+Χειρολαβή",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "780",
      "name": "Μάσκες Προστ Προσώπου 50τεμ",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "781",
      "name": "Παυλίδης Κουβερτούρα Κλασ 125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "782",
      "name": "Σολομός Νωπός Φιλετ/νος Με Δέρμα Υδ Νορβ/Εισαγ  Β.Α Ατλ Συσκ/νος",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "783",
      "name": "Soflan Υγρό Απορ Ρούχ Μαλλ/Ευαισθ 950ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "784",
      "name": "Dr Beckmann Καθαριστικο Φουρνου 375ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "785",
      "name": "Dettol Υγρό Πολυκαθαριστικό Αντιβακτηριδιακό 500ml Sparkling Lemon & Lime Burst Power & Fresh",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "786",
      "name": "Soupline Mistral Μαλακτικό Συμπ 82πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "787",
      "name": "Ροδόπη Αριάνι 1,7% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "788",
      "name": "Martini Bianco Απεριτίφ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "789",
      "name": "Misko Παραδ Χυλοπίτες Με Αυγά Μετσόβου 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "790",
      "name": "Λάπα Βόειου Α/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "791",
      "name": "Garnier Express Ντεμακιγιάζ Ματιών 2σε1 125ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "792",
      "name": "Jacobs Καφές Φίλτρου Εκλεκτός 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "794",
      "name": "Ντομάτες Εγχ Υπαιθρ Τσαμπί ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "795",
      "name": "Βιτάμ Μαργαρίνη Κλασικό 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "796",
      "name": "Μεβγάλ Παραδοσιακό Γιαούρτι Αγελαδ 220γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "797",
      "name": "Γιώτης Σιρόπι Σοκολάτα 350γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "798",
      "name": "Αρνιά Νωπά Ελλην Γαλ Ολοκλ Χ/Κ Χ/Σ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0936072fcb3947f3baf83e31bb5c1cab"
    },
    {
      "id": "799",
      "name": "Λαιμός Χοιρινός Μ/Ο Νωπός Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "800",
      "name": "Lipton Ice Tea Instant Λεμονι 125γρ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "801",
      "name": "Coca Cola 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "802",
      "name": "Αγγουράκια Κιλ Τυπ Νειλ – Τυπ Κνωσ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "803",
      "name": "Pom Pon Eyes & Face Μαντηλάκια 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "804",
      "name": "Dixan Υγρό Απορρυπαντικό Ρούχων Άνοιξης 30μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "805",
      "name": "Κρασί Της Παρέας Λευκό 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "806",
      "name": "Μεβγάλ Αριάνι 1,5% Χ Γλουτ 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "807",
      "name": "Veet Αποτριχωτική Κρέμα Κανον Επιδερμ 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "808",
      "name": "Ίον Σοκολάτες Γάλακτος 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "809",
      "name": "Αρκάδι Σαπούνι Πλάκα Πρασ 4Χ150γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "810",
      "name": "Υφαντής Μπέικον Καπνιστό Χ Γλουτ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "811",
      "name": "Pom Pon Μαντηλ Ντεμακ Sensit 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "812",
      "name": "Μινέρβα Χωριό Βούτυρο 41% Επαλ Σκαφ 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "814",
      "name": "Γιώτης Μείγμα Για Κρέπες 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "815",
      "name": "Lipton Χαμομήλι Φακ 10τεμΧ1γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "816",
      "name": "Άλτις Κλασσικό Ελαιόλαδο 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "817",
      "name": "Στεργίου Μηλόπιτα Ατομική 105γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47b5f0016f4f0eb79e3a4b932f7577"
    },
    {
      "id": "818",
      "name": "Νουνού Γάλα Family 1,5% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "821",
      "name": "Αύρα Φυσικό Μεταλλικό Νερό 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "823",
      "name": "Vanish Pink Πολυκαθαριστικό Λεκέδων 30γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "824",
      "name": "Στεργίου Κρουασάν Βιέννης Με Κρέμα Σοκολάτα 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "825",
      "name": "Nan Optipro Γάλα Τρίτης Βρεφικής Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "826",
      "name": "Veet Κρέμα Για Ευαίσθ Επιδ 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "827",
      "name": "7 Days Bake Rolls Pizza 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47b5f0016f4f0eb79e3a4b932f7577"
    },
    {
      "id": "828",
      "name": "Ferrero Rocher Πραλίνες 16τεμ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "829",
      "name": "Υφαντής Ferano Προσούτο Χ Γλουτ 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "830",
      "name": "Zest Familia Λουκανικοπιτάκια 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "831",
      "name": "Μάκβελ Μακαρόνια Σπαγγέτι Ν6 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "832",
      "name": "Ελιά Βόειου Α/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "833",
      "name": "Λεμόνια Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "836",
      "name": "Nivea Αφρόλουτρο Cream Care 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "837",
      "name": "Ariel Alpine Απορ Σκόνη 2,925γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "838",
      "name": "Dorodo Τυρί Τριμμ Φακ 80γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "839",
      "name": "Uncle Bens Ρύζι 10 λεπτά 4Χ125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "840",
      "name": "Σπάλα Βόειου/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "841",
      "name": "Κατσέλης Κριτσίνια Μακεδονικά Ολικής Άλεσης 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "842",
      "name": "Tasty Φουντούνια 105γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "f87bed0b4b8e44c3b532f2c03197aff9"
    },
    {
      "id": "843",
      "name": "Ω3 Αυγά Αμερικ Γεωργ Σχολής 6τ Large 63-73γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d2babbc7355444ca0d27633207e4743"
    },
    {
      "id": "844",
      "name": "Όλυμπος Γάλα Ζωής Λευκό Υψ Παστ 1,5% Λ 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "845",
      "name": "Όλυμπος Γάλα Επιλεγμ. 3,7% Λ 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "846",
      "name": "Hellmann's Μουστάρδα Απαλή 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "847",
      "name": "Dettol Υγρό Καθαριστικό Αντιβακτηριδιακό Κουζινας 500ml Με Ενεργο Οξυγονο Power & Pure",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "848",
      "name": "Βλάχα Χυλοπιτάκι Με Αυγά 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "849",
      "name": "Κύκνος Τοματοπολτός 28% Μεταλ 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5aba290bf919489da5810c6122f0bc9b"
    },
    {
      "id": "850",
      "name": "Dr Beckmann Καθαρ Πλυν Ρούχ 250γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "851",
      "name": "Gillette Gel Ξυρ Μοιsture 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "852",
      "name": "Κατσίκια Νωπά Ελλην Γαλ Ολοκλ Χ/Κ Χ/Σ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d3385ff161f0423aa364017d4413fa77"
    },
    {
      "id": "853",
      "name": "Πατάτες  Ελλ Κατ Α Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "854",
      "name": "Lipton Τσάι Κίτρινο Φακ 20τεμΧ1,5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "855",
      "name": "Λουμίδης Καφές Ελληνικός 96γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "856",
      "name": "Vapona Σκοροκτόνα Φύλλα 20τμχ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "8f98818a7a55419fb42ef1d673f0bb64"
    },
    {
      "id": "857",
      "name": "Rio Mare Τόνος Λαδιού 2Χ160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "858",
      "name": "Danone Activia Επιδ Τραγαν Απολ Δημ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "859",
      "name": "Sani Lady Sensitive Super N5 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "0bf072374a8e4c40b915e4972990a417"
    },
    {
      "id": "860",
      "name": "Klinex Σπρέυ 4σε1 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "861",
      "name": "Fix Hellas Μπύρα 6X330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "862",
      "name": "Fissan Baby Κρέμα 50γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "863",
      "name": "Alfa Κασερόπιτα Πηλίου Κατεψυγμένη 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "864",
      "name": "Johnson's Baby Μπατονέτες Βαμβ 100τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "866",
      "name": "Όλυμπος Γιαούρτι Στραγγιστό 10% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "867",
      "name": "Όλυμπος Γιαούρτι Στραγγιστό 2% 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "868",
      "name": "Ίον Σοκοφρέτα Μίνι Σακουλάκι 210γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "869",
      "name": "Ultrex Σαμπουάν Γυναικ Κανον 360ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "870",
      "name": "Κύκνος Τοματοπολτός 410γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5aba290bf919489da5810c6122f0bc9b"
    },
    {
      "id": "872",
      "name": "Μπρόκολα Πράσινα Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "873",
      "name": "Misko Τορτελίνι Με Τυρί 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "874",
      "name": "Παπαδοπούλου Φρυγανιές Χωριάτικες 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "875",
      "name": "Αύρα Νερό Μεταλ Μπλουμ 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "876",
      "name": "Βλάχας Γάλα Εβαπορέ Ελαφρύ 410γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "877",
      "name": "Δέλτα Smart Επιδ Γιαουρ Φραουλ 2Χ145γρ +1δώρο",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "878",
      "name": "Γαύρος Νωπός Καθαρ Απεντ/νος Ελλην Μεσογ Συσ/Νος",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c487e038079e407fb1a356599c2aec3e"
    },
    {
      "id": "879",
      "name": "Φάγε Total Γιαούρτι Στραγγιστό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "880",
      "name": "Μεβγάλ Παραδοσιακό Γιαούρτι Προβ 220γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "881",
      "name": "Μπριζόλες Καρέ/Κόντρα Χοιρ Νωπές Ελλ Μ/Ο ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "882",
      "name": "Χρυσή Ζύμη Μπουγάτσα Θεσ/Κης Κρέμα 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "883",
      "name": "Μέλισσα Κριθαράκι Μέτριο 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "884",
      "name": "Λακώνια Χυμός Νέκταρ Πορ/Μηλ/Βερ 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "885",
      "name": "Ace Gentile Ενισχυτικό Πλύσης 1lt",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "887",
      "name": "Knorr Ζωμός Κότας 12 κυβ 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "888",
      "name": "Colgate Οδ/Μα Sensation Whiten.75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "889",
      "name": "Almiron-1 Γάλα Σε Σκόνη Πρώτης Βρεφικής Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "890",
      "name": "Dettol All In 1 Πράσινο Μήλο 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "891",
      "name": "Κορπή Φυσικό Μεταλλικό Νερό1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "892",
      "name": "Χρυσή Ζύμη Κρουασάν Βουτύρου 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "894",
      "name": "Ίον Σοκοφρέτα Γάλακτος 38γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "895",
      "name": "Μπάρμπα Στάθης Μπάμιες Extra 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "896",
      "name": "Κοτοπουλα Ολοκληρα Νωπα Χυμα Τ.65% Π.Α.Ελλην",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "897",
      "name": "Παπαδημητρίου Balsamico Βιολογικό Καλαμάτας 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "898",
      "name": "Nivea Γαλάκτ Καθαρ Ξηρ/ Ευαίσθ Επιδ 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "899",
      "name": "Everyday Σερβ Super/Ultra Plus Sens 18τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "900",
      "name": "Babycare Μωροπ/τες Αντ/κο 3Χ72τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "92680b33561c4a7e94b7e7a96b5bb153"
    },
    {
      "id": "901",
      "name": "Μπανάνες Υπολ Μάρκες ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "902",
      "name": "Mythos Μπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "903",
      "name": "Παυλίδης Σοκολάτα Υγείας Αμύγδ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "904",
      "name": "Όλυμπος Φυσικός Χυμός Πορτοκάλι 1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "905",
      "name": "Κρεμμύδια Κόκκινα Ξερά Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "906",
      "name": "Νουνού Γάλα Συμπ Μερίδες Διχ 10Χ15γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "907",
      "name": "Sanitas Παγοκυψέλες 2 Σε 1",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "908",
      "name": "Υφαντής Hot Dog Nuggets Κοτόπουλου 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "909",
      "name": "Υφαντής Γαλοπούλα Καπνιστή 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "910",
      "name": "Κύκνος Χυμ Τομάτας Συμπ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "911",
      "name": "7 Days Τσουρεκάκι Κλασικό 75γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0e1982336d8e4bdc867f1620a2bce3be"
    },
    {
      "id": "912",
      "name": "Maggi Κύβοι Ζωμού Κότας 6λιτ 12τεμ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "913",
      "name": "Gouda Τυρί Φάγε Φέτες 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "914",
      "name": "Μιμίκος Κοτόπουλο Φιλ Μπούτ Νωπό Τυποπ 650γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "463e30b829274933ab7eb8e4b349e2c5"
    },
    {
      "id": "915",
      "name": "Alpro Ρόφημα Αμύγδαλο Χ Γλουτ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "916",
      "name": "Καρπούζια Μίνι Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "917",
      "name": "Veet Ταινίες Κρύο Κερί 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "918",
      "name": "Γιώτης Ανθός Αραβοσίτου Βανίλια 43γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "919",
      "name": "Maggi Μείγμα Λαχανικών Νοστιμιά Σε Σκόνη 130γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "920",
      "name": "Ωμέγα Special Ρύζι Basmati 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "921",
      "name": "Ajax Άσπρος Σίφουνας Λεμόνι 1000ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "922",
      "name": "Dove Αφροντούς Deep Nour 500ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "923",
      "name": "Syoss Σαμπ Όγκο 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "924",
      "name": "Forno Bonomi Μπισκ Σφολιατ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "925",
      "name": "Neomat Total Eco Απορ Τριαν 14πλ 700γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "926",
      "name": "Nestle Smarties Κουφετάκια Σοκολ 38γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "927",
      "name": "Septona Σαμπουάν Και Αφρόλουτρο Βρεφικό Με Λεβαντα 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "928",
      "name": "Amstel Μπύρα Premium Quality 0,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "929",
      "name": "Kellogg’s Δημητριακά Corn Flakes 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "931",
      "name": "Ferrero Kinder Pingui Σοκ/Γκοφρ 4X124γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "932",
      "name": "Λακώνια Φυσ Χυμός Πορτοκάλι 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "933",
      "name": "Bic Ξυρ Μηχ Classic 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "934",
      "name": "Dettol Αντιβ Υγρό Κρεμοσ Ευαίσθ Επιδερμ Αντ/κο 250ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "935",
      "name": "Μεβγάλ Κρέμα Βανίλια 150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "936",
      "name": "Dettol Απολυμαντικό Για Ρούχα",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "937",
      "name": "Nan Optipro 2 Γάλα Σε Σκόνη Δεύτερης Βρεφικής Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "938",
      "name": "Alfa Λουκανικοπιτάκια Κουρού 800gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "939",
      "name": "Ήπειρος Φέτα Ποπ Σε Άλμη 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "940",
      "name": "ΣΟΥΡΩΤΗ Μεταλλικό Νερό Ανθρ Λεμον 330ml ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "941",
      "name": "Friskies Σκυλ/Φή Ξηρ Κοτ/Λαχ 1,5κιλ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "942",
      "name": "Friskies Γατ/Φή Πατέ Κοτ/Λαχ 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "943",
      "name": "Proderm Υγρό Απορ/κο 17μεζ 1250ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "991276688c8c4a91b5524b1115122ec1"
    },
    {
      "id": "944",
      "name": "Αλλατίνη Φαρίνα Κέικ Φλάουρ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "945",
      "name": "Στεργίου Λουκουμάς 4τεμ 340γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47b5f0016f4f0eb79e3a4b932f7577"
    },
    {
      "id": "946",
      "name": "Κανάκι Pizza Special 3 Χ 460γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3f38edda7854447a837956d64a2530fa"
    },
    {
      "id": "947",
      "name": "Gillette Venus Ξυρ Γυν Ανταλ 4τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "948",
      "name": "Αλλατίνη Κέικ Βανίλια Με Κακάο 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "949",
      "name": "Gillette Fusion Αντ/κα Ξυραφ 4τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "950",
      "name": "Regilait Γάλα Αποβ/Νο Σε Σκόνη 250γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "951",
      "name": "Pedigree Υγ Σκυλ/Φή 3 Ποικ Πουλερικών 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "952",
      "name": "Όλυμπος Τυρί Χωριάτικο Σε Άλμη 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "953",
      "name": "Νουνού Γάλα Εβαπορέ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "954",
      "name": "Everyday Σερβ Norm/Ultra Plus Sens 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "955",
      "name": "Lurpak Soft Αλατισμένο 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "956",
      "name": "Neslac Επιδόρπιο Γάλακτος Μπισκότο 4Χ100γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "957",
      "name": "Κρι Κρι Σπιτικό Επιδόρπιο Γιαουρτιού 5% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "959",
      "name": "Σπάλα Νεαρού Μοσχ Α/Ο Νωπή Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c2ce05f4653c4f4fa8f39892bbb98960"
    },
    {
      "id": "960",
      "name": "Μεβγάλ Γάλα Αγελ Λευκό 3,5% Λιπ 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "961",
      "name": "La Vache Qui Rit Τυρί 8τμχ 140γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "962",
      "name": "Γιώτης Αλεύρι Φαρίνα Πορτοκαλί 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "963",
      "name": "Johnson's 24η Κρ Ημ Essentials Hydr SPF15 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "964",
      "name": "Johnson's Baby Σαμπουάν 750ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "965",
      "name": "Γιώτης Σοκολάτα Sweet/Balance Χ Γλουτ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "966",
      "name": "Elvive Color Vive Μάσκα Μαλ 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "967",
      "name": "3 Άλφα Φακές Ψιλές Εισαγωγής 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "968",
      "name": "Pemα Ψωμί Σικ Ολ Άλεσης 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "970",
      "name": "Nescafe Classic Στιγμιαίος Καφές 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "971",
      "name": "Gillette Blue Ii Plus Slalom Sensit 5τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "972",
      "name": "Δωδώνη Γιαούρτι Στραγγιστό 2% 1Kg",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "973",
      "name": "Νουνού Γάλα Εβαπορέ Light 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "974",
      "name": "Agrino Ρύζι Parboiled Bella Χ Γλουτ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "975",
      "name": "Pedigree Denta Stix Small Σκύλου 110γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "976",
      "name": "Delica Χαρτομάντηλα Αυτοκινήτου Λευκά Big 150τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "977",
      "name": "Nivea After Shave Balsam Sens 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "978",
      "name": "Δομοκού Τυρί Κατίκι Ποπ 200g",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "979",
      "name": "Maggi Barilla Spaghettoni No7 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "981",
      "name": "Νίκας Σαλάμι Αέρος 72 Πικάντ Χ Γλ 165γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "982",
      "name": "Septona Σερβιέτες Sensitive Ultra Plus Night 8τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "983",
      "name": "Κανάκι Λουκανικοπιτάκια Κατεψυγμένα 920γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "984",
      "name": "Παπαδοπούλου Krispies Ολικής Χωρίς Ζάχαρη 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "985",
      "name": "Nestle Fitness 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "988",
      "name": "Παυλίδης Γκοφρέτα 3bit 31γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "989",
      "name": "Gillette Fusion Proglide Power Ανταλ 3 τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "990",
      "name": "Ζωγράφος Φρουκτόζη 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a885d8cd1057442c9092af37e79bf7a7"
    },
    {
      "id": "993",
      "name": "Pampers Πάνες Μωρού Premium Pants Nο 5 12-17κιλ 34τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "994",
      "name": "Νουνού Γάλα Εβαπορέ Light 170γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "995",
      "name": "Κοτόπουλα Νωπά Ολόκλ Τ.65% Μιμίκος  Π.Α.Ελλην Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "997",
      "name": "Kleenex Χαρτί Υγείας 2 Φύλλα 12τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "998",
      "name": "Overlay Κρέμα Επίπλων 250ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "999",
      "name": "Silvo Γυαλιστικό Ασημικών 150ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1000",
      "name": "Whiskas Γατ/Φή Κοτόπουλο 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "1001",
      "name": "Νίκας Σαλαμι Αέρος Συκευασμενο 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "1002",
      "name": "Cutty Sark Ουίσκι 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1003",
      "name": "Skip Σκόνη Regular 45πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1004",
      "name": "Cajoline Συμπυκνωμένο Μαλακτικό Blue Fresh 30μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1005",
      "name": "Sensodyne Οδ/μα Complete Protection 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "1006",
      "name": "Proderm Kids Αφρόλουτρο Χαμομήλι 700ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "1007",
      "name": "Skip Σκόνη Spring Fresh 45μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1008",
      "name": "Νουνού Γάλα Family Υψ Θερ Επ Light 1,5% 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1009",
      "name": "Φάγε Total Γιαούρτι 5% 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1010",
      "name": "Γιώτης Κορν Φλάουρ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "1011",
      "name": "Svelto Gel Υγρό Πιάτων Με Ξύδι 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1012",
      "name": "Everyday Σερβ Extr Long/Ultra Plus Sens 10τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1013",
      "name": "Le Petit Marseillais Μάσκα Μαλλ Ξηρ 300ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "cf079c66251342b690040650104e160f"
    },
    {
      "id": "1015",
      "name": "Κατσίκια Νωπά Ελλην Γαλ Ολοκλ Μ/Κ Μ/Σ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d3385ff161f0423aa364017d4413fa77"
    },
    {
      "id": "1016",
      "name": "Ajax Τζαμ Crystal Clean Αντ/Κο 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1017",
      "name": "Γιώτης Mείγμα Παγωτού Καιμάκι 508γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "1018",
      "name": "Peppa Pig Φρουτοποτό Τροπ Φτούτα 250ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1019",
      "name": "Παπαδοπούλου Μπισκότα Πτι Μπερ Ν16 225γ 16τεμ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "35cce434592f489a9ed37596951992b3"
    },
    {
      "id": "1020",
      "name": "Ferrero Kinder Γάλακτοφέτες 5Χ140γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1021",
      "name": "Τσίπουρα Υδατ Ελλην G 400/600 Μεσογ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "1022",
      "name": "Quaker Τραγανές Μπουκ Σοκολ Υγείας 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "1024",
      "name": "Sprite 6X330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1025",
      "name": "Παπαδημητρίου Κρεμά Βαλσαμ Χ Γλ 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1026",
      "name": "Moscato D'Αsti Casarito Κρασί 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "1028",
      "name": "Ava Υγρό Πιάτων Action Λευκο Ξυδι Αντλια 650ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1029",
      "name": "Dirollo Τυρί Ημισκλ 14% Λιπ Φετ 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1031",
      "name": "Vaseline Petroleum Jelly 100% Καθαρή Βαζελίνη 100 ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "fefa136c714945a3b6bcdcb4ee9e8921"
    },
    {
      "id": "1032",
      "name": "Παπαδοπούλου Τριμμα Φρυγανιας Τριμμα 180γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "1033",
      "name": "Στήθος Φιλέτο Κοτ Ελλην. Νωπό Συσκ/Νο",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "1034",
      "name": "Πορτοκ Μερλίν - Λανε Λειτ- Ναβελ Λειτ Εγχ Χυμ Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "1035",
      "name": "Johnson Baby Βρεφικό Σαμπουάν Χαμομήλι Αντλιά 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "1036",
      "name": "Αρνιά Νωπά Ελλην Γαλ Τεμ Χ/Κ Χ/Σ Συσκ/Νο",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0936072fcb3947f3baf83e31bb5c1cab"
    },
    {
      "id": "1037",
      "name": "Life Χυμός Φυσικός Πορτοκάλι 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1038",
      "name": "Μέλισσα Μακαρόνια Σπαγγετίνη Νο 10 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1039",
      "name": "Κιχί Πίτα Με Πράσο Ταψί Κατεψυγμένο 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1040",
      "name": "Χρυσή Ζύμη Τυροπιτάκια Κουρου 920γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1041",
      "name": "Vidal Αφρόλ White Musk 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1043",
      "name": "Μεβγάλ Only 2% Et Συρτ 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1044",
      "name": "Παπαδημητρίου Κρέμα Balsamico Λευκή 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "1045",
      "name": "Όλυμπος Βούτυρο Αγελ Πακ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1046",
      "name": "Ντομάτες Εγχ Υπαιθρ Β ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "1047",
      "name": "Ariel Υγρό Απορρυπαντικό Ρούχων Alpine 28μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1048",
      "name": "Φάγε Total Γιαούρτι Στραγγιστό 2% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1049",
      "name": "Κρις Κρις Ψωμί Τοστ Σταρένιο 700gr",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "1050",
      "name": "Overlay Ultra Spray Λιποκαθαριστής Λεμόνι 650ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1051",
      "name": "Bonne Maman Μαρμελάδα Βερικ Χ Γλ 370γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1052",
      "name": "Orzene Σαμπουάν Μπύρας Κανον 400ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1053",
      "name": "Νουνού Τυρί Γκουντα Light 11% Φετ 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1054",
      "name": "Γιώτης Κακάο 125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "1055",
      "name": "Agrino Φασόλια Γίγαντες Ελέφαντες Καστοριάς Π.Γ.Ε. 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "1056",
      "name": "Μεβγάλ Κεφίρ Φράουλα 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1057",
      "name": "Oral B Οδοντικό Νήμα Κηρωμένο 50τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "1058",
      "name": "Ίον Σοκολ Αμυγδ Υγείας 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1059",
      "name": "Αττική Μέλι 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "1060",
      "name": "Χωριό Ελαιόλαδο Κορωνεική Ποικ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "1061",
      "name": "Νουνού Γάλα Σκόνη Frisolac 1ης Βρεφ Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "1062",
      "name": "Λουμίδης Καφές Ελληνικός 194γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1063",
      "name": "Gillette Blue Ii Fixed Head 5τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1064",
      "name": "Κύκνος Κέτσαπ Χ Γλουτ 330γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1065",
      "name": "Κατσίκια Νωπά Ελλην Γαλ Τεμ Χ/Κ Χ/Σ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d3385ff161f0423aa364017d4413fa77"
    },
    {
      "id": "1066",
      "name": "Pom Pon Μαντ Καθαρ Argan Oil 20τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "1067",
      "name": "Adoro Βούτυρο 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1068",
      "name": "Τσίπουρα Υδατ Ελλην Β 200/300 Μεσογ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "1069",
      "name": "Μύλοι Αγίου Γεωργίου Αλεύρι Για Πίτσα 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "1070",
      "name": "Φλώρινα Ξυνό Νερό 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "1071",
      "name": "Κεραμάρη Μάννα Αλεύρι Για Πίτες 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "1072",
      "name": "Στεργίου Τσουρέκι 380γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0e1982336d8e4bdc867f1620a2bce3be"
    },
    {
      "id": "1073",
      "name": "Bref Wc Power Active Αρωματικό Τουαλέτας Πεύκο 50γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1074",
      "name": "Danone Activia Επιδ Γιαουρ Ακτιν 2Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1075",
      "name": "Pummaro Χυμός Τομάτα Πιο Συμπ/Νος 520γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1076",
      "name": "Nescafe Classic Στιγμιαίος Καφές 50γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1077",
      "name": "Μεταξά 3 Μπράντυ 350ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1078",
      "name": "Johnson's Baby Αφρόλουτρο Μπλε 750ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "1079",
      "name": "Zewa Χαρ Υγείας Ultra Soft 8τεμ 912γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "034941f08ca34f7baaf5932427d7e635"
    },
    {
      "id": "1080",
      "name": "Nan Optipro Γάλα Τρίτης Βρεφικής Ηλικίας 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "1081",
      "name": "Maggi Κύβοι Ζωμού Λαχανικών 6λιτ 12τεμ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "1082",
      "name": "Hellmann's Κέτσαπ 560γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "1083",
      "name": "Palmolive Αφρόλ Natural Αμυγδ 650ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1084",
      "name": "Nivea Visage Ημερ Kρ Απαλ Ενυδ Spf15 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "1085",
      "name": "OralB Οδ/Mα 1/2/3 75ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "26e416b6efa745218f810c34678734b2"
    },
    {
      "id": "1086",
      "name": "Kellogg's Δημητριακά Choco Pops Chocos 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "1087",
      "name": "Φάγε Μιγμ Tριμ 4 Τυρ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1088",
      "name": "Στεργίου Κέικ Ανάμικτο 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "1089",
      "name": "Ντομάτες Εισ Α",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "1090",
      "name": "Λαιμός Χοιρινός Μ/Ο Νωπός Ελλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a73f11a7f08b41c081ef287009387579"
    },
    {
      "id": "1091",
      "name": "Everyday Σερβ/Κια Norm All Cotton 24τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1092",
      "name": "Ρεπάνη Αγιωργίτικος Ερυθρός Οίνος 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "1093",
      "name": "Παπαδοπούλου Ψωμί Τόστ Plus Σίτου 700γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "1094",
      "name": "Λακωνία Φυσικός Χυμός Πορτοκάλι 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1095",
      "name": "Παν Κρέμα Βαλσάμικο 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "1096",
      "name": "Νουνού Γάλα Family 3,6% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1097",
      "name": "Καλλιμάνης Χταπόδι Μικρό 595γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "1098",
      "name": "Κανάκι Φύλλο Κρούστας Νωπό 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "1099",
      "name": "Green Cola 1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1100",
      "name": "Nestle Fitness Dark Chocolate 375γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "1101",
      "name": "La Vache Qui Rit Τυρί Φέτες Light 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1102",
      "name": "Johnson Βρέφικη Πουδρα Σωματος 200γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "1103",
      "name": "Ίον Σοκοφρέτα Γάλακτ Με Φουντούκ 38γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1104",
      "name": "Alfa Τριγωνάρια Με Τυρί Ανεβατο Κατεψυγμένα 750γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1105",
      "name": "Fairy Original All in One Καψ Πλυντ Πιάτ Λεμόνι 22τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1106",
      "name": "Barilla Σάλτσα Βασιλικος 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ce4802b6c9f44776a6e572b3daf93ab1"
    },
    {
      "id": "1107",
      "name": "Haribo Goldbaren Καραμ Ζελίνια Αρκουδ 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7cfe21f0f1944b379f0fead1c8702099"
    },
    {
      "id": "1109",
      "name": "Γιώτης Ρυζόγαλο Στιγμής 105γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "1111",
      "name": "Ούζο 12 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1112",
      "name": "Βλάχας Γάλα Εβαπορέ Πλήρες 410γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1113",
      "name": "Μεβγάλ Harmony 1% Με Μέλι/Γκραν 164γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1114",
      "name": "Scotch Brite Σύρμα Πράσινο Κουζίνας",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1115",
      "name": "Μέλισσα Κριθαράκι Χονδρό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1116",
      "name": "Κορπή Νερό 6Χ1,5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "1117",
      "name": "Χρυσή Ζύμη Τυροπίτα Σπιτική 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1118",
      "name": "Μηλοκλέφτης Μηλίτης 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1119",
      "name": "Sani Υποσέντονα Fresh Maxi Plus 15τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "0bf072374a8e4c40b915e4972990a417"
    },
    {
      "id": "1120",
      "name": "Μέγα Βαμβάκι 100γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "af538008f3ab40989d67f971e407a85c"
    },
    {
      "id": "1121",
      "name": "Sanitas Αλουμινόχαρτο 30μ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1122",
      "name": "Quanto Μαλακτικό Ρούχων Ελληνικά Νησιά 18μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1123",
      "name": "Scotch Brite Σφουγγ Κουζ Γίγας Αντιβ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1124",
      "name": "Νίκας Μπέικον Καπνιστό Συσκευασμένο 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "1125",
      "name": "Atrix Κρέμα Χερ Intens Χαμομήλι 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "fefa136c714945a3b6bcdcb4ee9e8921"
    },
    {
      "id": "1126",
      "name": "Septona Σαμπουάν Και Αφρόλουτρο Βρεφικό Με Αλοη 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "1127",
      "name": "Υφαντής Κεφτεδάκια Κτψ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "1128",
      "name": "Μακβελ Μακαρόνια Σπαγγέτι No 10 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1129",
      "name": "Fouantre Γαλοπούλα Σε Φέτες 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "1130",
      "name": "Becel Pro Activ Ρόφημα Γιαουρ Φράουλα 4Χ100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1131",
      "name": "Nescafe Dolce Gusto Espresso Int Καψ 16x7γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b89cb8dd198748dd8c4e195e4ab2168e"
    },
    {
      "id": "1132",
      "name": "Ροδόπη Γιαούρτι Πρόβειο Βιο 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1133",
      "name": "Pillsbury Ζύμη Φρέσκια Σφολιάτας 700γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "1134",
      "name": "Τοπ Ξύδι Κοκκίνου Κρασιού 350ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "1137",
      "name": "Dettol Κρεμ Sensitive Αντ/κο 750ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "1138",
      "name": "Μεβγάλ Harmony 1% Ανανάς 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1139",
      "name": "Wella Flex Mousse Curles/Waves 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "1140",
      "name": "Αττική Μέλι 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "1141",
      "name": "Babylino Πάνες Μωρού Sensitive Nο7 17+ κιλ 14τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "1142",
      "name": "Klinex Καθ Πατώματος Λεμόνι 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1143",
      "name": "Always Σερβ Night 9τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1144",
      "name": "Κλεοπάτρα Σαπούνι 125γρ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "1145",
      "name": "Danone Activia Επιδ Γιαουρ Καρυδ/Βρώμη 2Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1146",
      "name": "Nan Optipro 1 Γάλα Σε Σκόνη Πρώτης Βρεφικής Ηλικίας 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "1147",
      "name": "Μεβγάλ Topino Απαχο Γάλα Κακάο 310ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1149",
      "name": "Pampers Πάνες Premium Care Nο 4 8-14 κιλ 52τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "1150",
      "name": "Serkova Βότκα 37,5% 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1151",
      "name": "Μπάρμπα Στάθης Σαλάτα Καλαμπ 450γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "1152",
      "name": "Μέλισσα Σπαγγέτι Ολικής Άλεσης 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1153",
      "name": "Δέλτα Γάλα Πλήρες 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1154",
      "name": "Heineken Μπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1155",
      "name": "Δέλτα Advance Επιδ Αλεσμένα Δημητρ 2Χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1156",
      "name": "Quaker Νιφ Βρώμης Ολ Άλεσης Μεταλ 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "1157",
      "name": "Ντομάτες Εγχ Υπαιθρ Α ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "1159",
      "name": "Μήλα Φουτζι Εγχ ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "1160",
      "name": "Fina Τυρί Φέτες 10% Λιπ 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1161",
      "name": "Fix Hellas Mπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1162",
      "name": "Μεβγάλ High Protein Φρα Drink 237ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1163",
      "name": "Babylino Sensitive No4 Econ 7-18κιλ 50τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "1164",
      "name": "Μεβγάλ Στραγγιστό Γιαούρτι 2% 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1165",
      "name": "Ζωγράφος Μαρμελ Φράουλ Φρουκτ 415γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e397ddcfb34a4640a42b8fa5e999b8c8"
    },
    {
      "id": "1166",
      "name": "Μπάρμπα Στάθης Αρακάς Λαδερός 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "6d084e8eab4945cdb4563d7ff49f0dc3"
    },
    {
      "id": "1167",
      "name": "L'Oreal Studio Line Fx Gel Extra Fix 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "1169",
      "name": "Όλυμπος Γάλα Επιλεγμ 1,5% Λ 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1170",
      "name": "Απαλαρίνα Λικέρ Μαστίχα 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1171",
      "name": "Ready2U Μάσκες Προστ Προσώπου 50τεμ",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "1172",
      "name": "Dove Ντούς Deeply Nourisηing 750ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1173",
      "name": "Μεβγάλ Γάλα Αγελ Λευκό Light 1,5% 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1174",
      "name": "COVER 50τεμ Μάσκ Με Λάστιχο 1 Χρήση",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "1175",
      "name": "Hansaplast Universal Αδιάβροχα 40τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "1b59d5b58fb04816b8f6a74a4866580a"
    },
    {
      "id": "1176",
      "name": "Dettol Κρεμοσάπουνο 250ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "9c86a88f56064f8588d42eee167d1f8a"
    },
    {
      "id": "1177",
      "name": "Swiffer Πανάκια Αντ/Κα 16τεμ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1178",
      "name": "Stella Artois Μπύρα 6x330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1179",
      "name": "Pampers Premium Care No 5 11-18κιλ 44τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "1180",
      "name": "Campari Bitter Aπεριτίφ 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1181",
      "name": "Κρεμμύδια Ξανθά Ξερά Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "1182",
      "name": "Bacardi Ρούμι 700ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1183",
      "name": "Lurpak Soft Μειωμέν Λιπαρ Ανάλ 225γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1184",
      "name": "Μεβγάλ Γάλα «Κάθε Μέρα» 1.5% 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1185",
      "name": "Rol Σκόνη Για Πλυσ Στο Χέρι 380γρ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1186",
      "name": "Λαυράκια Υδατ  Καθαρ Ελλην400/600 Μεσογ Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "1187",
      "name": "Gillette Fusion 5 Proglide Ξυρ Μηχ+Ανταλ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1188",
      "name": "Dettol Κρεμ Relax Αντ/κο 750ml",
      "category": "e4b4de2e31fc43b7b68a0fe4fbfad2e6",
      "subcategory": "8f1b83b1ab3e4ad1a62df8170d1a0a25"
    },
    {
      "id": "1190",
      "name": "Johnson Baby Βρεφικό Σαμπουάν Αντλιά 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "1191",
      "name": "Vileda Style Κουβάς",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1192",
      "name": "Νουνού Γάλα Family 3,6% 1,5λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1193",
      "name": "Always Σερβ Ultra Platinum Night 12τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1195",
      "name": "Μινέρβα Χωριό Eλαιόλαδο Εξαιρ Παρθ 4λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "1196",
      "name": "Purina Gold Gourmet Γατ/Φή Βοδ/Κοτ 85γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "1197",
      "name": "Κύκνος Τοματοχυμός 390ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1198",
      "name": "Λουξ Σόδα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1199",
      "name": "Derby Ίον 38γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1200",
      "name": "Klinex Υγρό Καθαρισμού Μπάνιου Spray 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1201",
      "name": "Μπρόκολα Πράσινα Εισ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9bc82778d6b44152b303698e8f72c429"
    },
    {
      "id": "1202",
      "name": "Becel Pro Activ Μαργαρίνη Σκαφ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1203",
      "name": "Leerdammer Τυρί Τοστ Special 125γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1204",
      "name": "Ήρα Αλάτι Ψιλό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "1205",
      "name": "Κύκνος Τοματάκι Ψιλοκ Χαρτ Συσκ 370γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1206",
      "name": "Τοπ Κρέμα Βαλσάμικο Με Λεμόνι & Μέλι 200ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "1207",
      "name": "Knorr Ζωμός Σπιτικός Φρεσκ Λαχανικ 4Χ28γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3935d6afbf50454595f1f2b99285ce8c"
    },
    {
      "id": "1208",
      "name": "Τσίπουρα Υδατ  Καθαρ Ελλην G 400/600 Μεσογ Συσκ/Νη",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "1209",
      "name": "Τσίχλες Trident Δυόσμος 8γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7cfe21f0f1944b379f0fead1c8702099"
    },
    {
      "id": "1210",
      "name": "Ίον Σοκολάτα Γάλακτος Αμυγδάλου 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1211",
      "name": "Sanitas Αλουμινόχαρτο 10μετ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "b5d54a3d8dd045fb88d5c31ea794dcc5"
    },
    {
      "id": "1212",
      "name": "Nivea Black/White Invisible 48h Rollon 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "1213",
      "name": "Axe Αποσμ Σπρέυ Dark Temptation 150ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "35410eeb676b4262b651997da9f42777"
    },
    {
      "id": "1214",
      "name": "COVER 10τεμ Μάσκ Με Λάστιχο 1 Χρήση",
      "category": "2d5f74de114747fd824ca8a6a9d687fa",
      "subcategory": "79728a412a1749ac8315501eb77550f9"
    },
    {
      "id": "1215",
      "name": "Kerrygold Τυρί Regato 270γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1216",
      "name": "Gillette Ξυρ Μηχ Mach 3 Turbo+Ανταλ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2df01835007545a880dc43f69b5cae07"
    },
    {
      "id": "1217",
      "name": "Ίον Σοκολάτα Γάλακτος 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1219",
      "name": "Νεκταρίνια Εγχ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ea47cc6b2f6743169188da125e1f3761"
    },
    {
      "id": "1220",
      "name": "7 Days Swiss Roll Κακάο 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "e63b2caa8dd84e6ea687168200859baa"
    },
    {
      "id": "1222",
      "name": "Pampers Πάνες Μωρού Premium Care Newborn 2-5κιλ 26τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "1223",
      "name": "Μεβγάλ Στραγγιστό Γιαούρτι 2% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1225",
      "name": "Κρίς Κρίς Ψωμί Τόστ Μπρίος 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "1226",
      "name": "Johnson's Baby Oil Ενυδατικό Λάδι, 300ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "1227",
      "name": "Αρνιά Νωπά Ελλην Γαλ Τεμ Χ/Κ Χ/Σ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0936072fcb3947f3baf83e31bb5c1cab"
    },
    {
      "id": "1228",
      "name": "Ίον Σοκολάτα Αμυγδάλου 70γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1229",
      "name": "Becel Pro Activ Ελαιόλαδο 35% Λιπ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1230",
      "name": "Γιώτης Αλεύρι Φαρίνα Κόκκινη 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "1231",
      "name": "Trata Σαρδέλα Πικάντικη 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "1232",
      "name": "Ajax Υγρό Γενικού Καθαρισμού Kloron Lila 1λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1233",
      "name": "Elite Φρυγανιές Ολικής Άλεσης 180γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a483dd538ecd4ce0bdbba36e99ab5eb1"
    },
    {
      "id": "1235",
      "name": "Χρυσή Ζύμη Χωριάτικο Φυλλο Κατεψυγμένο 700γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "1236",
      "name": "Misko Μακαρόνια Σπαγγέτι Ν5 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1237",
      "name": "Cool Hellas Χυμός Πορτοκαλ Συμπ 1λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1238",
      "name": "Μεβγάλ Πολίτικο 2Χ150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "509b949f61cc44f58c2f25093f7fc3eb"
    },
    {
      "id": "1239",
      "name": "Μίνι Babybel Διχτάκι 6τεμ 120γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1241",
      "name": "Ariel Υγρές Καψ 3σε1 Κανονικό 24πλ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1242",
      "name": "Pedigree Schmackos Μπισκότα Σκύλου 43γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "0c6e42d52765495dbbd06c189a4fc80f"
    },
    {
      "id": "1243",
      "name": "Γιώτης Ανθός Ορύζης 150γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "1244",
      "name": "Κοτόπουλα Νωπά Ολόκλ Τ.65% Π.Α.Ελλην Συσκ/Να",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "8ef82da99b284c69884cc7f3479df1ac"
    },
    {
      "id": "1245",
      "name": "Ήρα Αλάτι Μαγειρικό 1kg",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2ad2e93c1c0c41b4b9769fe06c149393"
    },
    {
      "id": "1246",
      "name": "Crunch Σοκολάτα Λευκή 100γρ Χωρίς Γλουτένη",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1247",
      "name": "Μεβγάλ High Protein Choc Drink 242ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1248",
      "name": "Εβόλ Γάλα Παστερ Διαλεχτο 3,7% Λ 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1249",
      "name": "Nestle Φαρίν Λακτέ 350γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "7e86994327f64e3ca967c09b5803966a"
    },
    {
      "id": "1250",
      "name": "Ζωγράφος Μακαρόνια Διαίτης Ν6 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1251",
      "name": "Καραμολέγκος Πίτες Για Σουβλ Σταρεν 10τεμ 820γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1252",
      "name": "Όλυμπος Γιαούρτι Στρ 2% Freelact 2Χ170γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1253",
      "name": "Pescanova Μπακαλιάρος Φιλέτο 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "7ca5dc60dd00483897249e0f8516ee91"
    },
    {
      "id": "1254",
      "name": "Στάμου Γιαούρτι Πρόβειο Παραδ 240γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1255",
      "name": "Pampers Active Baby No4+ 10-15κιλ 16τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "1256",
      "name": "Γιώτης Αλεύρι Φαρίνα Ολικής Άλεσης 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "1257",
      "name": "Κύκνος Τομάτες Αποφλ Ολoκλ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1258",
      "name": "Nivea Κρέμα Ξυρίσματος 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "1259",
      "name": "Misko Μακαρόνια Για Παστίτσιο Ν2 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0c347b96540a427e9823f321861ce58e"
    },
    {
      "id": "1260",
      "name": "Kellogg's Special K Μπάρα Δημητριακών Με Ξηρούς Καρπούς Καρύδα Και Κασioυς 4Χ28γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "916a76ac76b3462baf2db6dc508b296b"
    },
    {
      "id": "1261",
      "name": "Βέρμιον Νάουσα Κομπόστα Ροδάκινο 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "df10062ca2a04789bd43d18217008b5f"
    },
    {
      "id": "1262",
      "name": "Chipita Frau Lisa Bάση Τούρτας Κακάο 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "1263",
      "name": "Εν Ελλάδι Μπέικον Καπνιστό Σε Φέτες 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "1264",
      "name": "Everyday Σερβ Norm/Ultra Plus Sens 18τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1265",
      "name": "Everyday Σερβ Super/Ultra Plus Hyp 18 τεμ",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "2bce84e7df694ab1b81486aa2baf555d"
    },
    {
      "id": "1266",
      "name": "Γιώτης Sanilac 3 Γάλα Σκόνη 400γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "1267",
      "name": "Amita Motion Φυσικός Χυμός 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "4f1993ca5bd244329abf1d59746315b8"
    },
    {
      "id": "1268",
      "name": "Persil Black Υγρό Απορ Πλυντ Ρούχ 12Μεζ 750ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1269",
      "name": "Heineken Μπύρα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1270",
      "name": "Creta Farms Εν Ελλάδι Κοτομπουκιές Κτψ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "9b7795175cbc4a6d9ca37b8ee9bf5815"
    },
    {
      "id": "1271",
      "name": "Δέλτα Milko Κακάο 500ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1272",
      "name": "Alfa Μπουγάτσα Θες/νίκης Κρέμα 800γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "d1315c04b3d64aed93472e41d6e5a6f8"
    },
    {
      "id": "1273",
      "name": "Leerdammer Τόστ Light 10 φέτες 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1274",
      "name": "Ζωγράφος Καστανή Ζάχαρη 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a885d8cd1057442c9092af37e79bf7a7"
    },
    {
      "id": "1275",
      "name": "Κορπή Νερό 6χ0,5ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "1276",
      "name": "Παπαδημητρίου Balsamico Με Μέλι 250ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5dca69b976c94eccbf1341ee4ee68b95"
    },
    {
      "id": "1277",
      "name": "Μεβγάλ Harmony 1% Ροδακινο 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1278",
      "name": "3 Άλφα Φασόλια Χονδρά Εισαγωγής 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "50e8a35122854b2b9cf0e97356072f94"
    },
    {
      "id": "1279",
      "name": "Sol Ηλιέλαιο 1λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "1280",
      "name": "Corona Μπύρα Extra 355ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "329bdd842f9f41688a0aa017b74ffde4"
    },
    {
      "id": "1281",
      "name": "Λεβέτι Κασέρι Ποπ Φέτες 175γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1282",
      "name": "3 Άλφα Ρύζι Νυχάκι Ελληνικό 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "1283",
      "name": "Adoro Κρέμα Γάλακτος 35% Λιπαρά 200ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4e4cf5616e0f43aaa985c1300dc7109e"
    },
    {
      "id": "1284",
      "name": "Καραμολέγκος Παξαμάς Κρίθινος 600γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "1285",
      "name": "Pummaro Ψιλοκ Τοματ Κλασ 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1286",
      "name": "Nivea After Shave Balsam 100ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "e2f81e96f70e45fb9552452e381529d3"
    },
    {
      "id": "1287",
      "name": "Morfat Κρέμα Σαντιγύ Μετ 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "1288",
      "name": "Μπάρπα Στάθης Τομάτα Στον Τρίφτη 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a02951b1c083449b9e7fab2fabd67198"
    },
    {
      "id": "1289",
      "name": "L'Oreal Excellence Βαφή Μαλ Ξανθό Ν7",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "09f2e090f72c4487bc44e5ba4fcea466"
    },
    {
      "id": "1290",
      "name": "Fissan Baby Bagnetto Υποαλ Σαμπουάν/Αφρόλ 500ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "3d0c29b055f8417eb1c679fbfdc37da0"
    },
    {
      "id": "1291",
      "name": "Knorr Quick Soup Μανιτ Με Κρουτόν 36γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eef696c0f874603a59aed909e1b4ce2"
    },
    {
      "id": "1292",
      "name": "Pampers Πάνες Premium Care Nο 3 5-9 κιλ 60τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "1293",
      "name": "Almiron-2 Γάλα Σε Σκόνη Δεύτερης Βρεφικής Ηλικίας 800γρ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "fc71b59318b5410d8ed9da8b42904d77"
    },
    {
      "id": "1294",
      "name": "Babylino Πάνες Μωρού Sensitive 16+ κιλ No 6 15τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "e0efaa1776714351a4c17a3a9d412602"
    },
    {
      "id": "1295",
      "name": "Kit Kat Σοκολάτα 41,5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1296",
      "name": "Fytro Ζάχαρη Καστανή Ακατέργαστη 500γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a885d8cd1057442c9092af37e79bf7a7"
    },
    {
      "id": "1297",
      "name": "Γιώτης Αλεύρι Για Όλες Τις Χρήσεις 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c761cd8b18a246eb81fb21858ac10093"
    },
    {
      "id": "1298",
      "name": "Lenor Gold Orchid 56μεζ 1,4λιτ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "3be81b50494d4b5495d5fea3081759a6"
    },
    {
      "id": "1299",
      "name": "Knorr Ρύζι Risonatto Milanaise 220γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "5d0be05c3b414311bcda335b036202f1"
    },
    {
      "id": "1301",
      "name": "Lipton Τσάι Ρόφημα 10 Φακ 1,5γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "2d711ee19d17429fa7f964d56fe611db"
    },
    {
      "id": "1303",
      "name": "Μεβγάλ Harmony 1% Φράουλα 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1304",
      "name": "Μεβγάλ Only 0% Et Συρτ 3Χ200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1305",
      "name": "Lay's Πατατάκια Ρίγανη150γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "1306",
      "name": "Παπαδοπούλου Krispies Σουσάμι 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "bcebd8cc2f554017864dbf1ce0069ac5"
    },
    {
      "id": "1307",
      "name": "Άλτις Ελαιόλαδο Δοχείο 4λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "1308",
      "name": "Μινέρβα Χωριό Μαργαρίνη Με Ελαιόλαδο 250γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1309",
      "name": "Μινέρβα Χωριό Φέτα Ποπ Βιολ Άλμη 350γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1310",
      "name": "L'Oreal Κρέμα Προσ Καν/Μικτ Επιδ 3 Φρον 50ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5a2a0575959c40d6a46614ab99b2d9af"
    },
    {
      "id": "1311",
      "name": "Μεβγάλ Τριμμένο Τυρί Light 10% Λ 200γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1313",
      "name": "Μεβγάλ Γιαούρτι Πρόβειο Παραδ 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1314",
      "name": "Haig Ουίσκι 0,7λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "08f280dee57c4b679be0102a8ba1343b"
    },
    {
      "id": "1315",
      "name": "Baby Care Μωρομάντηλα Χαμομήλι Minipack 12τεμ",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "92680b33561c4a7e94b7e7a96b5bb153"
    },
    {
      "id": "1316",
      "name": "Μινέρβα Χωριό Ορεινές Περιοχές Ελαιόλαδο Παρθένο 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1e9187fb112749ff888b11fd64d79680"
    },
    {
      "id": "1317",
      "name": "Κρι Κρι Σπιτικό Επιδόρπιο Γιαουρτιού 2% 1κιλ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1318",
      "name": "Νέα Φυτίνη Φυτικό Μαγειρικό Λίπος 400γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a240e48245964b02ba73d1a86a2739be"
    },
    {
      "id": "1319",
      "name": "Friskies Adult Ξηρά Γατ/Φή Βοδ/Συκ/Κοτ 400γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "1320",
      "name": "Botanic Therapy Σαμπουάν Επανόρθ 400ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "46b02b6b4f4c4d5d8a0efe21d0981027"
    },
    {
      "id": "1321",
      "name": "Γιώτης Κουβερτούρα Σε Σταγόνες 100γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1322",
      "name": "Παπαδοπούλου Ψωμί Σίτου Φυσ Προζύμι 700γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c928573dd7bc4b7894d450eadd7f5d18"
    },
    {
      "id": "1323",
      "name": "Whiskas Γατ/Φή Πουλ Σε Σάλτσα 100γρ",
      "category": "662418cbd02e435280148dbb8892782a",
      "subcategory": "926262c303fe402a8542a5d5cf3ac7eb"
    },
    {
      "id": "1324",
      "name": "Ίον Σοκολάτα Γάλακτος 45γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "dca17e0bfb4e469c93c011f8dc8ab512"
    },
    {
      "id": "1325",
      "name": "Ζαγόρι Νερό 500ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    },
    {
      "id": "1326",
      "name": "Σαρδέλλες Νωπές Καθαρ Απεντ/νες Ελλην Μεσογ Συσκ/Νες",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c487e038079e407fb1a356599c2aec3e"
    },
    {
      "id": "1327",
      "name": "Tuborg Σόδα 330ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3010aca5cbdc401e8dfe1d39320a8d1a"
    },
    {
      "id": "1329",
      "name": "Cheetos Pacotinia 114γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "ec9d10b5d68c4d8b8998d51bf6d67188"
    },
    {
      "id": "1330",
      "name": "Εβόλ Γάλα Παστερ Κατσικ Βιολ 590ml",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1331",
      "name": "Γιώτης Τούρτα Μιλφέιγ 532γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "a1a1c2c477b74504b58ad847f7e0c8e1"
    },
    {
      "id": "1332",
      "name": "Soupline Συμπυκνωμένο Μαλακτικό Ρούχων Λεβάντα 28μεζ",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1333",
      "name": "Στεργίου Κρουασάνάκια Με Γέμιση Πραλίνα 300γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "19c54e78d74d4b64afbb1fd124f01dfc"
    },
    {
      "id": "1336",
      "name": "Chicco Βρέφική Κρέμα Συγκάματος 100ml",
      "category": "8016e637b54241f8ad242ed1699bf2da",
      "subcategory": "ddb733df68324cfc8469c890b32e716d"
    },
    {
      "id": "1337",
      "name": "Υφαντής Γαλοπούλα Βραστή 160γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "be04eae3ca484928a86984d73bf3cc3a"
    },
    {
      "id": "1338",
      "name": "Σολομός Νωπός Φέτα Μ/Δ & Μ/Ο  Υδ Νορβ/Εισαγ  Β.Α Ατλ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "3d22916b908b40b385bebe4b478cf107"
    },
    {
      "id": "1339",
      "name": "Μεβγάλ Παραδ Γιαούρτι Αιγοπρ Ελαφ 2Χ220γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1340",
      "name": "Φάγε Τρικαλινό Τυρί Ζάρι Φάγε 380γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "4c73d0eccd1e4dde8bb882e436a64ebb"
    },
    {
      "id": "1341",
      "name": "Calliga Demi Sec Ροζέ Οίνος 750ml",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "3d01f4ce48ad422b90b50c62b1f8e7f2"
    },
    {
      "id": "1342",
      "name": "Palmolive Υγρό Πιάτων Regular 500ml",
      "category": "d41744460283406a86f8e4bd5010a66d",
      "subcategory": "e60aca31a37a40db8a83ccf93bd116b1"
    },
    {
      "id": "1343",
      "name": "Μεβγάλ Harmony Gourm ΑλατΚαραμ /Dark Choc 165γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "0364b4be226146699140e81a469d04a1"
    },
    {
      "id": "1344",
      "name": "Χρυσή Ζύμη Χορτοπίτα Σπιτική 850γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "1eb56e6ffa2a449296fb1acc7b714cc5"
    },
    {
      "id": "1345",
      "name": "Wella Flex Mousse Ultra Strong 200ml",
      "category": "8e8117f7d9d64cf1a931a351eb15bd69",
      "subcategory": "5935ab588fa444f0a71cc424ad651d12"
    },
    {
      "id": "1346",
      "name": "Ferrero Kinder Αυγό Εκπλ Χ Γλουτ 20γρ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b1866f1365a54e2d84c28ad2ca7ab5af"
    },
    {
      "id": "1347",
      "name": "Δέλτα Γάλα 2λιτ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "b3992eb422c2495ca02dd19de9d16ad1"
    },
    {
      "id": "1348",
      "name": "Σαρδέλλες Νωπές Ελλην Μεσογ Ε/Ζ",
      "category": "ee0022e7b1b34eb2b834ea334cda52e7",
      "subcategory": "c487e038079e407fb1a356599c2aec3e"
    },
    {
      "id": "1352",
      "name": "Αύρα Φυσικό Μεταλλικό Νερό 1.5λιτ",
      "category": "a8ac6be68b53443bbd93b229e2f9cd34",
      "subcategory": "bc4d21162fbd4663b0e60aa9bd65115e"
    }
  ]
    '''

    product_data = json.loads(json_data)
    save_product_images(product_data)

if __name__ == "__main__":
    main()