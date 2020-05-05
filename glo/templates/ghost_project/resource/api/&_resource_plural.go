package &_{resource_name}

import (
	"github.com/limoxi/ghost"
	dm_&_{resource_name} "&_{service_name}/domain/model/&_{resource_name}"
)

type &_{resource_title_plural} struct {
	ghost.ApiTemplate
}

type &_{resource_plural}GetParams struct {
	Filters ghost.Map `form:"filters"`
	WithOptions ghost.FillOptions `form:"with_option"`
	CurPage int `form:"cur_page"`
	PageSize int `form:"page_size"`
}

func (this *&_{resource_title_plural}) Resource() string{
	return "&_{resource_name}.&_{resource_plural}"
}

func (this *&_{resource_title_plural}) Get() ghost.Response{
	var params &_{resource_plural}GetParams
	this.Bind(&params)
	ctx := this.GetCtx()
	&_{resource_name}Repository := dm_&_{resource_name}.New&_{resource_title}Repository(ctx)
	paginator := ghost.NewPaginator(params.CurPage, params.PageSize)
	&_{resource_name}Repository.SetPaginator(paginator)
	&_{resource_plural} := dm_&_{resource_name}.New&_{resource_title}Repository(ctx).GetByFilters(params.Filters)
	dm_&_{resource_name}.New&_{resource_title}FillService(ctx).Fill(&_{resource_plural}, params.WithOptions)
	return ghost.NewJsonResponse(ghost.Map{
		"&_{resource_plural}": dm_&_{resource_name}.New&_{resource_title}EncodeService(ctx).EncodeMany(&_{resource_plural}),
		"page_info": paginator.ToResultMap(),
	})
}

func init(){
	ghost.RegisterApi(&&_{resource_title_plural}{})
}
