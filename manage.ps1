<#
.SYNOPSIS
    Project management script for Windows (replaces Makefile).

.DESCRIPTION
    Provides commands to install dependencies, run tests, lint code, format code, and debug the template.

.EXAMPLE
    .\manage.ps1 install
    .\manage.ps1 test
    .\manage.ps1 lint
    .\manage.ps1 format
    .\manage.ps1 debug
#>

param (
    [Parameter(Mandatory=$true, Position=0)]
    [ValidateSet("install", "test", "lint", "format", "debug")]
    [string]$Command
)

$ErrorActionPreference = "Stop"

function Run-Command {
    param ([string]$Cmd, [string[]]$Arguments)
    Write-Host "> $Cmd $Arguments" -ForegroundColor Cyan
    & $Cmd $Arguments
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Command failed with exit code $LASTEXITCODE"
    }
}

switch ($Command) {
    "install" {
        Write-Host "Installing dependencies..." -ForegroundColor Green
        Run-Command "uv" "sync"
        
        if (Test-Path ".vscode/settings.json.example") {
            Write-Host "Configuring VS Code settings..." -ForegroundColor Green
            Copy-Item ".vscode/settings.json.example" ".vscode/settings.json" -Force
        }
    }

    "test" {
        Write-Host "Running tests..." -ForegroundColor Green
        Run-Command "uv" "run", "pytest", "-v", "tests/"
    }

    "lint" {
        Write-Host "Linting code..." -ForegroundColor Green
        Run-Command "uv" "run", "ruff", "check", "--fix", "."
    }

    "format" {
        Write-Host "Formatting code..." -ForegroundColor Green
        # Fix import sorting
        Run-Command "uv" "run", "ruff", "check", "--select", "I", "--fix", "."
        # Format code
        Run-Command "uv" "run", "ruff", "format", "."
    }

    "debug" {
        Write-Host "Debugging template generation..." -ForegroundColor Green
        $DebugDir = Join-Path $env:TEMP "debug_project"
        
        if (Test-Path $DebugDir) {
            Remove-Item $DebugDir -Recurse -Force
        }

        # Generate project
        Run-Command "cookiecutter" ".", "--no-input", "--output-dir", $DebugDir

        Write-Host "✅ Debug project created successfully!" -ForegroundColor Green
        Write-Host "📁 Location: $DebugDir" -ForegroundColor Yellow
        Write-Host "To explore: cd $DebugDir" -ForegroundColor Yellow
    }
}
