package &_{resource_name}

import (
	"github.com/limoxi/ghost"
)

type &_{resource_title} struct {
	ghost.BaseDBModel

}
func (&_{resource_title}) TableName() string{
	return "&_{resource_name}_&_{resource_name}"
}

func init(){
	ghost.RegisterDBModel(&&_{resource_title}{})
}