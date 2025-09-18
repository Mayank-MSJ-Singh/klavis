import http.client, json

conn = http.client.HTTPConnection("localhost", 3000)

payload = json.dumps({
  "username": "mayanksingh8713491@gmail.com",
  "password": "71821@Metabase"
})

headers = { "Content-Type": "application/json" }

conn.request("POST", "/api/session", body=payload, headers=headers)

res = conn.getresponse()
data = json.loads(res.read().decode())

print(data)  # {"id": "session_token_here"}
