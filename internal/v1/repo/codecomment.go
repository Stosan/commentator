package repo

import (
	"commentator/pkg/schemas"
	"gorm.io/gorm"
	"commentator/pkg/datamodels"
)

type CommentatorRepo struct {
	Db *gorm.DB
}

func NewCommentatorRepository(db *gorm.DB) *CommentatorRepo {
	return &CommentatorRepo{db}
}

// UserRepo implements the repository.UserRepository interface
var _ CommentatorRepoInterface = &CommentatorRepo{}

// CampaignService : interface for Radio Station model and operations on it
type CommentatorRepoInterface interface {
	//create a Campaign
	AddCodeToDB(r *datamodels.UserData) (string, error)
}

func (db *CommentatorRepo) AddCodeToDB(r *datamodels.UserData) (string, error) {

	cd_entity:=&schemas.CodeComment{Code: r.CodeBody, CodeLanguage: r.Language,CodeWithComment: r.CodeWithComment}
	// Create the campaign portfolio entity
	db.Db.Create(&cd_entity)

	return cd_entity.CodeWithComment, nil
}



