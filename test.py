key="WggnOxa5VgqEAWlvXLDDaod0Eq4MUPnEqUCwhqhIze6AR5GbxndNTmL_QUJvJPCnlWbadA."
from bardapi import Bard

token = key
bard = Bard(token=token,timeout=30)
code = '''
Add inline comprehensive commenting to this code and do nothing else:
func DetectProgrammingLanguage(function string) string {
	// Convert the function to lowercase for case-insensitive comparison
	function = strings.ToLower(function)

	if function[:3]=="def"{
		return "Python"
	} else if function[:4]=="func" {
		return "Go"
	} else if function[:8]=="function"{
		return "JavaScript"
	}

	return "Unknown"
}

'''
print(bard.get_answer(f"{code}")['content'])