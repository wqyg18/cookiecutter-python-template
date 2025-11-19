<#
.SYNOPSIS
    Project management script for Windows (replaces Makefile).

.DESCRIPTION
    Provides commands to install dependencies, run tests, lint code, and format code.

.EXAMPLE
    .\manage.ps1 install
    .\manage.ps1 test
    .\manage.ps1 lint
    .\manage.ps1 format
#>

param (
    [Parameter(Mandatory=$true, Position=0)]
    [ValidateSet("install", "test", "lint", "format")]
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
        
        if (-not (Test-Path ".git")) {
            Write-Host "Initializing Git repository..." -ForegroundColor Green
            Run-Command "git" "init"
        }

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
}
