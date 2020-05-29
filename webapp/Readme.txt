
Run python will get local server running.
API function can be tested in browser as follows:
http://127.0.0.1:8050/api/md/spot?ticker=amzn&val_dt=2020-5-1

VBA project must add reference "Microsoft Scripting Runtime".
If the web api returns object it must be in json format. Json can be decomposed by thirdparty vba macro JsonConverter:
"Dim jsonObject As Object: Set jsonObject = JsonConverter.ParseJson" It can be found at https://github.com/VBA-tools/VBA-JSON/blob/master/JsonConverter.bas


Function to get web api from VBA:

option explicit
option base 1

Function api_get(strReq as string) as string

on error goto errmsg

dim strUrl as string: strUrl = "http://127.0.0.1:8050/api/"+strReq + "&rnd=" &Cstr(Rnd)

dim hReq as Object
Set hReq = CreateObject("MSXML2.XMLHTTP")
	With hReq
		.Open "GET", strUrl, False
		.Send
	End With
	
Dim response As String: response = hReq.ResponseText

api_get = response

Exit Function
errmsg:

End Function
