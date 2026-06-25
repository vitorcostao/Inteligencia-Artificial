$pdfPath = Join-Path $PSScriptRoot "..\Atividade Prática 2 - Busca - Coração Eucarístico.pdf"
$bytes = [System.IO.File]::ReadAllBytes($pdfPath)
$text = [System.Text.Encoding]::GetEncoding("iso-8859-1").GetString($bytes)

# Extract text between BT and ET markers
$matches = [regex]::Matches($text, 'BT\s*(.*?)\s*ET', [System.Text.RegularExpressions.RegexOptions]::Singleline)

foreach($m in $matches) {
    $inner = $m.Groups[1].Value
    $tjMatches = [regex]::Matches($inner, '\((.*?)\)')
    foreach($tj in $tjMatches) {
        Write-Host $tj.Groups[1].Value -NoNewline
    }
    Write-Host ""
}
