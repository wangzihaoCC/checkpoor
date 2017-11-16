/*
说明：
obj：检测值，默认当前对象的value值
type：检测对象类型
n:检测方法标识
optins：自定义检测方法
Repeat:是否检测重复性（默认为false）
m：重复性检测位数（默认为0）
方法成功后返回为true或者false，失败返回null
为防止转义符“\”，把原来的“\”改为“\\”
*/
;(function($,jQuery, window, document){
	var Verify_ku=
	{
		name:[{'0':'\\d*'},{'1':'[a-z]*'},{'2':'\\w*'},{'3':'[\\u4e00-\\u9fa5]*'},],
		/*用户名验证*/
		Password:[{'0':'\\w{6,}'},{'1':'\\w*'}],
		/*密码验证*/
		Mobile:[{'0':'1(3|4|5|7)d{9}'}],
		/*手机验证*/
		phone:[{'0':'\\d{3}-\d{8}|\\d{4}-\\d{7}'}],
		/*固定电话验证*/
		ID_number:[{'0':'\\d{15}|\\d{18}'}],
		/*身份证号验证*/
		Email:[{'0':'\\w+([-+.]\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*'}],
		/*邮箱验证*/
		Postcode:[{'0':'[1-9]\\d{5}'}],
		/*邮政编码验证*/
		Digital:[{'0':'\\D*'}],
		/*非数字验证*/
		Chinese:[{'0':'\\W*'}],
		/*中文验证*/
		B_license:[{'0':'\\d{15}'}],
		/*营业执照验证*/
	};
	var ceshi=function(ele,opt){
		this.Verify_opt={
			'obj':$(ele).val(),
			'type':null,
			'n':0,
			'optins':null,
			'Repeat':false,
			'm':0,
		};
		this.options=$.extend({},this.Verify_opt,opt);
	};
	ceshi.prototype={
		int:function(){			
			if(this.options.obj&&this.options.type){
				if(!this.options.Repeat && this.options.m==0){
						return 1;
				}else if(this.options.Repeat && this.options.m!=0){
						return 2;
				}else{
					return null;
				}
				
				
			}else{
				return null;
			}
		},
		//重复检测
		Verify_Repeat:function(){
			var n=0;	
			for(var i=0;i<this.options.obj.length;i++){
				var a=this.options.obj.substring(i,i+1);
				for(var g=0;g<this.options.obj.length;g++){
					var b=this.options.obj.substring(g,g+1);
					if(a==b){
						n++;
						if(n>=this.options.m){					
							return false;
						}
					}
				}
				n=0;		
			}
			return true;
		},
		//正则验证
		Verify_Verify:function (){
			var this_options='';
			if(this.options.optins){this_options=this.options.optins}
			else{
				for( var typ in Verify_ku){
					if(typ==this.options.type){					
						for(var kk in Verify_ku[this.options.type]){
							if(kk==this.options.n){						
								$.each(Verify_ku[this.options.type][this.options.n],function(i,k){
									this_options=k;
								});
							}
						}
					}
				}
			}			
			this_options='/^'+this_options+'$/';			
			this_options=eval(this_options);			
			if(this_options.test(this.options.obj)==false){
				return false;
			}else{
				return true;
			}
			
		}
	
	};
	$.fn.Verify=function(options){
		var cs= new ceshi(this,options);
		if(cs.int()==1){			
			if(cs.Verify_Verify()){
				return true;
			}else{
				return false;
			}			
		}else if(cs.int()==2){
			if(!cs.Verify_Verify()&&!cs.Verify_Repeat()){
				return false;
			}else{
				return true;
			}
		}else{
			return null;
		}
	}
})(jQuery, window, document);
