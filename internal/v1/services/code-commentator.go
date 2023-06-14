package services

import (
	"commentator/internal/config"
	"commentator/internal/v1/repo"
	"commentator/internal/v1/utils"
	d "commentator/pkg/datamodels"
	"context"
	"fmt"
	"net/http"

	"github.com/go-playground/validator"
	"github.com/labstack/echo/v4"
	openai "github.com/sashabaranov/go-openai"
	"gorm.io/gorm"
)

type CodeCommentData struct {
	Db *gorm.DB
	rs repo.CommentatorRepoInterface
}

func NewCodeComment(rs repo.CommentatorRepoInterface, db *gorm.DB) *CodeCommentData {
	return &CodeCommentData{
		Db: db,
		rs: rs,
	}
}

func (cm *CodeCommentData) MakeCodeComments(c echo.Context) error {
	code_commented_map := make(map[string]string)
	v := validator.New()
	userData := new(d.UserData)

	// Binding the request data to the UserData struct
	if err := c.Bind(&userData); err != nil {
		return c.JSON(http.StatusBadRequest, "invalid data")
	}

	// Validate the user data using the validator
	if err := v.Struct(userData); err != nil {
		return c.JSON(http.StatusExpectationFailed, "validation failed")
	}

	switch userData.Language {
	case "golang":
		lang_type := utils.DetectProgrammingLanguage(userData.CodeBody)
		fmt.Print(lang_type)
		if lang_type == "Go" {
			code_commented, err := GPT3(lang_type, userData.CodeBody)
			if err != nil {
				return c.JSON(http.StatusBadRequest, err.Error())
			}
			code_commented_map["result"] = code_commented
		}
	case "python":
		lang_type := utils.DetectProgrammingLanguage(userData.CodeBody)
		if lang_type == "Python" {
			code_commented, err := GPT3(lang_type, userData.CodeBody)
			if err != nil {
				return c.JSON(http.StatusBadRequest, err.Error())
			}
			code_commented_map["result"] = code_commented
		}
	case "javascript":
		lang_type := utils.DetectProgrammingLanguage(userData.CodeBody)
		if lang_type == "JavaScript" {
			code_commented, err := GPT3(lang_type, userData.CodeBody)
			if err != nil {
				return c.JSON(http.StatusBadRequest, err.Error())
			}
			code_commented_map["result"] = code_commented
		}
	default:
		fmt.Println("Unknown role.")
	}

	return c.JSON(http.StatusOK, code_commented_map)
}

func GPT3(msg, language string) (string, error) {

	prompt_definition := fmt.Sprintf("PROMPT: add an explanation of the function at the top of this %s code and add inline comprehensive commenting to this code.", language)
	prompt := prompt_definition + "\n" + msg

	client := openai.NewClient(config.AppConfig.OPENAPI_KEY)
	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT3Dot5Turbo,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: prompt,
				},
			},
		},
	)

	if err != nil {
		//err_resp:=fmt.Sprintf("ChatCompletion error: %v\n", err)
		return "", err
	}

	return resp.Choices[0].Message.Content, nil
}
