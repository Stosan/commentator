package schemas

import (
	"time"

	"gorm.io/gorm"
)


type AppOperationsLog struct {
	gorm.Model
	Logtype string
	Data string
	Source string
	Timegenerated time.Time
	Description string
}