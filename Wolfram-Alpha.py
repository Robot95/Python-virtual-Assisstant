import wolframalpha

input = raw_input("Q: ")
app_id = "YOUR APP ID" # No my app id
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print answer
