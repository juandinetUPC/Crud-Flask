# Crud-Flask
## En un entorno virtual usando Python3 , pip y la siguiente lista de dependencias (requirements.txt)
- flask



Si no está instalado, instalamos virtualenv

```powershell
pip install virtualenv
```

Para crear un ambiente virtual digitamos el siguiente comando:

```powershell
virtualenv -p python3 env
```

para poner a funcionar el entorno virtual, se debe ejecutar:

```powershell
.\env\Scripts\activate
```

Una vez iniciado el entorno virtual, se ejecuta el siguiente comando:

```powershell
pip install -r .\requirements.txt
```

Para correr la solución se ejecuta el siguiente comando:

```powershell
python .\src\app.py
```

Para correr los test unitarios se ejecuta el siguiente comando:

```powershell
python .\src\test_app.py
```
