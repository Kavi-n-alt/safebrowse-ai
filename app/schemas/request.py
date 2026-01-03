from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    url_length: int
    url_entropy: float
    num_subdomains: int
    contains_ip: int
    suspicious_tokens: int
    num_redirects: int
    external_domain_calls: int
    https_used: int
    script_count: int
    script_density: float
    inline_script_ratio: float
    permission_requests: int
    auto_downloads: int
    popup_count: int
    time_on_page: float
    repeat_visits: int
    session_frequency: int
