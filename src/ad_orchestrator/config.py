import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Config:
    domain: str
    dc_ip: str
    base_domain: str
    winrm_user: str
    winrm_password: str
    winrm_transport: str
    winrm_port: int


def load_config():
    if os.getenv("AD_VULNFORGE_MODE", "false").strip().lower() != "true":
        raise PermissionError("AD_VULNFORGE_MODE flag is set to false")

    domain = os.getenv("DOMAIN_NAME", "").strip().lower()
    if not domain.endswith((".local", ".lab")):
        raise ValueError("Domain must end with .local or .lab")

    try:
        domain = str(os.environ["DOMAIN_NAME"])
        dc_ip = str(os.environ["DC_IP"])
        base_domain = str(os.environ["BASE_DOMAIN"])
        winrm_user = str(os.environ["WINRM_USER"])
        winrm_password = str(os.environ["WINRM_PASSWORD"])
        winrm_transport = str(os.getenv("WINRM_TRANSPORT", "ntlm"))
        winrm_port = int(os.getenv("WINRM_PORT", "5985"))

        return Config(domain=domain, dc_ip=dc_ip, base_domain=base_domain, winrm_user=winrm_user,
                      winrm_password=winrm_password,winrm_transport=winrm_transport ,winrm_port=winrm_port)
    except KeyError as e:
        raise RuntimeError(f"Environment parameter is missing: {e}") from e







