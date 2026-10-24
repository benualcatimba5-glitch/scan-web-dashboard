# Scanner Ético Angola - Criado no Lobito
import requests

def scanner(site):
    try:
        print(f"[+] A verificar {site}...")
        r = requests.get(site, timeout=5)
        print(f"[OK] {site} -> Status: {r.status_code}")
        if r.status_code == 200:
            print(f"[SEGURO] {site} está online!")
        if 'https' in site:
            print(f"[BOM] {site} usa HTTPS")
    except:
        print(f"[ERRO] {site} fora do ar ou sem internet")

print("=== SCANNER ÉTICO LOBITO PROTECTOR ===")
scanner("https://www.google.com")
scanner("https://www.unitel.ao")
scanner("https://www.mpla.ao")
print("=== FIM DA VERIFICAÇÃO ===")