import requests
from time import sleep

API_KEY = "hhWoUakx0j23UecnW1TSZhctSG4RTohTaSQhxbjnUG6Kt8ezjz"    # Ask for your API key: https://web.plant.id/api-access-request/

class DatosPlantaController:
    def IdentifyPlant(self,file_names):
        img = str(file_names).encode
        params = {
            "images": img,
            "latitude": 49.1951239,
            "longitude": 16.6077111,
            "datetime": 1582830233,
            # Modifiers docs: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers
            "modifiers": ["crops_fast", "similar_images"],
            }

        headers = {
            "Content-Type": "application/json",
            "Api-Key": API_KEY,
            }

        response = requests.post("https://api.plant.id/v2/enqueue_identification",
                                json=params,
                                headers=headers).json()

        return self.get_result(response["id"])


    def get_result(self,identification_id):
        params = {
            "plant_language": "es",
            # Plant details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-details
            "plant_details": ["common_names",
                            "edible_parts",
                            "gbif_id",
                            "name_authority",
                            "propagation_methods",
                            "synonyms",
                            "taxonomy",
                            "url",
                            "wiki_description",
                            "wiki_image",
                            ],
            }

        headers = {
            "Content-Type": "application/json",
            "Api-Key": API_KEY,
            }

        endpoint = "https://api.plant.id/v2/get_identification_result/"

        while True:
            print("Waiting for suggestions...")
            sleep(2)
            response = requests.post(endpoint + str(identification_id),
                                    json=params,
                                    headers=headers).json()
            if response["suggestions"] is not None:
                return response
