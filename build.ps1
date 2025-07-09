$appname="AILiteSubtitler"
$outputDir = "install"
$sourceFile = "main.py" 

if (-Not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir
}

pyinstaller --onefile --name $appname -w src/$sourceFile --specpath . 
pyinstaller --onefile -w src/$sourceFile

Copy-Item -Path ".\dist\$appname.exe" -Destination "$outputDir\$appname.exe"

Remove-Item -Path "main.spec", "AILiteSubtitler.spec", "build", "dist" -Recurse -Force