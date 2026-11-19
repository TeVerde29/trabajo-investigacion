$docxPath = "c:\Users\hikih\Documents\Repositorios\trabajo-investigacion\ANÁLISIS BIBLIOMÉTRICO.docx"
$pdfPath = "c:\Users\hikih\.gemini\antigravity\brain\3c1cb7e3-0e2a-4f22-afe6-db3b1bb1be97\scratch\preview_no_prisma.pdf"

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($docxPath, $false, $true)
    $pages = $doc.ComputeStatistics(2)
    Write-Host "Document opened successfully. Total pages: $pages"
    $doc.ExportAsFixedFormat($pdfPath, 17)
    $doc.Close(0)
    Write-Host "PDF exported successfully to: $pdfPath"
} catch {
    Write-Error $_
} finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}
