
import json

def create_apikey(): 
    private_key_id = "93061333450aa8f471d7cd104a4e2841c54d29e5"
    private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCa+WxDrIkI+ftD\nxpzXOTqEa8SMj3KixKh0JGPdObElDj3gshADhGe1Xm0Us2OGLD8EGRwKxh9fXqMh\nukkp1XCNQibAIrfrtG4B7RmljcEv8P/ytnwcDLwN6ufSgXyfxdflumDJNBPLZcPJ\nbls+DI+wORiP6mvHTl+clcRKG1DA+N7nzBn5NgvjmjqNF1cq8sRsBXQm/hLrb/Fe\nZmPb0Mzri5XBVy6wMUipSg/PFMenSYMeMhojrIw7w2R7mq7KMtXwnFivbRNjpqVO\nVXCpWhAWBP0vnpcWeDnfsQoZeZ74S88VykQ07Qhhdg8eZUT662oD28ZZHvts2Ifj\nQcUqD2FLAgMBAAECggEAASvVmoghLwBIp4350HlkjLl0LlKSA+xNkGpX/auHQBrx\njJNIu+YSLJShz9BW3IQ7ShbwfdDA5762dLV/z3RtmdVNDd9If/XVbc4ZBzj6vUrq\nfEibYbdJuPQBO+q+z0XpzrKQABh7KWqqLKMMLUj5N9RuozCbD1INA4kKoNUmncnt\ngIafkDHWq9ETsmFR0NI1wr2GewfNk1njNkRhEB4OnJWSc9kmwRhm9HxYDKcuPcTF\nwNgdma7nwl82cp0LpMPUfhXL12rFlOftMJMb8FcwyjmTb/pdTj8pMXDIEGGAU4RD\n+CSypwLQkDPeuqfSHgSU14P6n+TjYBmCCU4xi5gZbQKBgQDS+ekVElN5B1PxDXE6\nm3wbgXTHOTWBMcrn2XUz18TcMmttzhQ1qy0WzQ+d/MMAnjn6bOdqObXtdjZvfL4A\nb8PrBzCE4RLKEux0e7Z/1r9HgWQ5L0DaZGcVE/nN4PSvFegl1jD2oWrnvhjBjSfl\nX738tA36hhwjKSTWljaA1QuUZQKBgQC8DAGsqjR2MqsehKdn5bbCeYkRHm2mlAlT\nqQYAXPzVQbAiQRk1kj6gHMjSKmBoUkrbo8QgOlT6AkvFYR7POFWP1V918AuEjw5j\noRs8+16a/FPTK1DtbfZZkPZKJMsSMch0renU79YUHwgOf1Slaevo/16z2x6DMiMp\nDNWxtKmL7wKBgHPcqQNYcBz8SD4OSsuLzglw+8fZBCgyRyMyiinxafwfeF3yGakr\nm3R1Iwl5YUH6ow6DNkdg8Cc7j0OEtveYaXiuFxgyXtY4tEB4HE5yidNkHL1G1Q/a\nqb2qnbpRuy5YEoiM65DWLtab0A6jTXCrNrQL0c1uTw+ELeXm0oHH/jb9AoGBAIae\nAcTdw9ipxR5/0GfsZr0pzBnZMp4Bc/vUEFvKNaVk9PZQq/9RxktQz+LEO2fzIWvC\n/PAlUhf39M5EDI5DwdzJ3yDKyzQGRULFXn51ZPCGmmudor2V7rmHsQi69jT8Nohw\nx+iMGTEmVdorBSm1fhC6X81Zm6pIBiuo6IHi1005AoGBAJq3aS9yo/xXZZ/OcoXW\ng2FZDRNwhIXfoetd5cGM6t2fe22vdcDoY3VFey8hvUd9e16tH2urDFCDA7u6AQqK\n/CGrFOVER0OosfP3ckpW4ijtGYot7j3sKRtbxkaU/nwn5On972pLzoWfS3azfMTv\nBz8K5Dh/7xq7IkLiO4gNz0Ac\n-----END PRIVATE KEY-----\n"
    client_id = "100221556918158372838"
    dictionary = {
    "type": "service_account",
    "project_id": "ai-learning-text-to-speech",
    "private_key_id": private_key_id,
    "private_key": private_key,
    "client_email": "my-tts-sa@ai-learning-text-to-speech.iam.gserviceaccount.com",
    "client_id": client_id,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/my-tts-sa%40ai-learning-text-to-speech.iam.gserviceaccount.com"
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("ai-learning-text-to-speech-93061333450a.json", "w") as outfile:
        outfile.write(json_object)