package repo

import (
	"commentator/pkg/datamodels"
)



type campaignApp struct {
	us CommentatorRepo
}

// UserApp implements the UserAppInterface
var _ CommentatorRepoInterface = &CommentatorRepo{}




func (u *campaignApp) AddCodeToDB(r *datamodels.UserData) (string, error){
	return u.AddCodeToDB(r)
}



