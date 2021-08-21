# Powershell

## Usefull commands

Open Explorer in current location:
```powershell
ii .
```

which is short for:
```powershell
Invoke-Item .
```

## Costumization

Using `Oh My Posh`:

Install with:
```powershell
Install-Module oh-my-posh -Scope CurrentUser
```

List themes:
```powershell
Get-PoshThemes
```

To apply a theme, edit `$PROFILE` and add the following line. 
```powershell
Set-PoshPrompt -Theme jandedobbeleer
```

Once added, reload your profile for the changes to take effect.
```powershell
. $PROFILE
```
