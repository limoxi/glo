package &_{resource_name}

import (
	"github.com/limoxi/ghost"
	bm_&_{resource_name} "&_{service_name}/business/model/&_{resource_name}"
)

type &_{resource_title} struct {
	ghost.ApiTemplate

	GetParams *struct {
	    Id int `form:"id"`
	    WithOptions ghost.FillOptions `form:"with_option"`
    }
    PutParams *struct {

    }
}

func (this *&_{resource_title}) Resource() string{
	return "&_{resource_name}.&_{resource_name}"
}

func (this *&_{resource_title}) Get() ghost.Response{
	ctx := this.GetCtx()
	params := this.GetParams
	&_{resource_name} := bm_&_{resource_name}.New&_{resource_title}Repository(ctx).GetById(params.Id)
	if &_{resource_name} != nil{
		panic(ghost.NewBusinessError("记录不存在"))
	}

    bm_&_{resource_name}.New&_{resource_title}FillService(ctx).Fill(&_{resource_name}, params.WithOptions)
	return ghost.NewJsonResponse(bm_&_{resource_name}.New&_{resource_title}EncodeService(ctx).Encode(&_{resource_name}))
}

func (this *&_{resource_title}) Put() ghost.Response{
	params := this.PutParams
	&_{resource_name} := bm_&_{resource_name}.New&_{resource_title}(this.GetCtx())
	return ghost.NewJsonResponse(ghost.Map{
		"id": &_{resource_name}.Id,
	})
}

func init(){
	ghost.RegisterApi(&&_{resource_title}{})
}
