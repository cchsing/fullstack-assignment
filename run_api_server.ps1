try{
    .\.venv\Scripts\Activate.ps1
    Set-Location .\part_3
    uvicorn api_server:app --reload
}
finally{
    Set-Location (Get-Item $MyInvocation.MyCommand.Source).Directory.FullName
    deactivate
}