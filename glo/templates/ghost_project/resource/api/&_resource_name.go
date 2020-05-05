package &_{resource_name}

import (
	"github.com/limoxi/ghost"
	dm_&_{resource_name} "&_{service_name}/domain/model/&_{resource_name}"
)

type &_{resource_title} struct {
	ghost.ApiTemplate
}

type &_{resource_name}GetParams struct {
	Id int `json:"id"`
}
type &_{resource_name}PutParams struct {

}

func (this *&_{resource_title}) Resource() string{
	return "&_{resource_name}.&_{resource_name}"
}

func (this *&_{resource_title}) Get() ghost.Response{
	var params &_{resource_name}GetParams
	this.Bind(&params)
	ctx := this.GetCtx()
	&_{resource_name} := dm_&_{resource_name}.New&_{resource_title}Repository(ctx).GetById(params.Id)
	if &_{resource_name} != nil{
		panic(ghost.NewBusinessError("记录不存在"))
	}
	return ghost.NewJsonResponse(dm_&_{resource_name}.New&_{resource_title}EncodeService(ctx).Encode(&_{resource_name}))
}

func (this *&_{resource_title}) Put() ghost.Response{
	var params &_{resource_name}PutParams
	this.Bind(&params)
	&_{resource_name} := dm_&_{resource_name}.New&_{resource_title}(this.GetCtx())
	return ghost.NewJsonResponse(ghost.Map{
		"id": &_{resource_name}.Id,
	})
}

func init(){
	ghost.RegisterApi(&&_{resource_title}{})
}
