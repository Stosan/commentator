package utils

import "strings"


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