# Study Break Generator backend

`app.py` contains the Flask API and the list of activities. `requirements.txt`
lists Flask and Gunicorn (the server used on Render). No database is needed.

## Run locally on Windows

From the project folder in PowerShell:

```powershell
cd study-break-backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:5000/break?minutes=5 in your browser. A sample response is:

```json
{"activity": "Stand up and stretch.", "minutes": 2}
```

The API randomly chooses an activity with an estimated duration less than or equal
to the requested time. Enter a positive whole number. Missing, invalid, zero, or
negative minutes return HTTP 400 with a JSON `error` message.

## Connect a webpage later

Use this JavaScript with the number entered by the user:

```javascript
async function getBreak(minutes) {
  const response = await fetch(
    `http://127.0.0.1:5000/break?minutes=${encodeURIComponent(minutes)}`
  );
  const data = await response.json();
  if (!response.ok) throw new Error(data.error);
  return data; // Display data.activity and data.minutes on your webpage.
}
```

The API permits cross-origin requests so a separately hosted webpage can use it.
After deployment, replace `http://127.0.0.1:5000` with your Render service URL.

## Deploy on Render

Push this project to a Git repository and connect it to a new Render Web Service.
Use these settings:

- Language: Python
- Root Directory: `study-break-backend`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`

Once deployed, visit `https://YOUR-SERVICE.onrender.com/break?minutes=5`.

References: [Render Flask guide](https://render.com/docs/deploy-flask) and
[root directory settings](https://render.com/docs/monorepo-support).
