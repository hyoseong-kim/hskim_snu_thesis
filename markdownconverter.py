# tools/md_to_pdf_pandoc.py
import subprocess
from pathlib import Path
import sys

# 경로 확인 (Raw string 사용 추천)
src = Path(r"c:\hskim_snu_thesis\hskim_snu_thesis\markdown.md")
out = src.with_suffix('.pdf')

cmd = [
    "pandoc",
    str(src),
    "-s",
    "--pdf-engine=xelatex",     # LaTeX 엔진 사용
    "-V", "mainfont=Malgun Gothic", # [중요] 한글 폰트 지정 (윈도우: 맑은 고딕)
    "--toc",
    "-o",
    str(out)
]

print("Running command:\n", " ".join(cmd))
print("-" * 20)

# capture_output=True를 해야 에러 메시지를 파이썬이 잡을 수 있습니다
res = subprocess.run(cmd, capture_output=True, text=True)

if res.returncode == 0:
    print("SUCCESS: Saved to", out)
else:
    print("FAILED: Error code", res.returncode)
    print("Error Message:\n", res.stderr) # <--- 여기에 진짜 에러 이유가 나옵니다
    sys.exit(res.returncode)