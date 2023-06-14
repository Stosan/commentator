package schemas

type CodeComment struct {
	ID              uint   `gorm:"primaryKey"`
	Code            string `gorm:"not null"`
	CodeWithComment string `gorm:"not null"`
	CodeLanguage    string `gorm:"not null"`
}
