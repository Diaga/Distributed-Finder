Search.setIndex({docnames:["autodocs/base","autodocs/commands","autodocs/db","autodocs/db.dao","autodocs/db.models","autodocs/main","autodocs/modules","commands","index","user_guide"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":3,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,sphinx:56},filenames:["autodocs/base.rst","autodocs/commands.rst","autodocs/db.rst","autodocs/db.dao.rst","autodocs/db.models.rst","autodocs/main.rst","autodocs/modules.rst","commands.rst","index.rst","user_guide.rst"],objects:{"":{base:[0,0,0,"-"],commands:[1,0,0,"-"],db:[2,0,0,"-"]},"base.arguments":{BaseArgument:[0,1,1,""],IntArgument:[0,1,1,""],StaticArgument:[0,1,1,""],StringArgument:[0,1,1,""]},"base.arguments.BaseArgument":{data:[0,2,1,""],reset:[0,2,1,""],validate:[0,2,1,""]},"base.arguments.IntArgument":{validate:[0,2,1,""]},"base.arguments.StaticArgument":{validate:[0,2,1,""]},"base.command":{BaseCommand:[0,1,1,""]},"base.command.BaseCommand":{arguments:[0,3,1,""],command:[0,3,1,""],get_input:[0,2,1,""],log:[0,2,1,""],match:[0,2,1,""],options:[0,3,1,""],reset:[0,2,1,""],run:[0,2,1,""],validate:[0,2,1,""]},"base.option":{Option:[0,1,1,""],StringOption:[0,1,1,""]},"base.option.Option":{reset:[0,2,1,""],validate:[0,2,1,""]},"base.terminal":{BaseTerminal:[0,1,1,""]},"base.terminal.BaseTerminal":{Context:[0,1,1,""],get_input:[0,2,1,""],get_prefix:[0,2,1,""],log:[0,2,1,""],match_command:[0,2,1,""],run:[0,2,1,""],sansio_run:[0,2,1,""]},"base.terminal.BaseTerminal.Context":{parse:[0,2,1,""],set_stdout:[0,2,1,""]},"commands.cat":{CatCommand:[1,1,1,""]},"commands.cat.CatCommand":{arguments:[1,3,1,""],command:[1,3,1,""],options:[1,3,1,""],run:[1,2,1,""],write_to_file:[1,2,1,""]},"commands.cat_at":{CatAtCommand:[1,1,1,""]},"commands.cat_at.CatAtCommand":{aliases:[1,3,1,""],arguments:[1,3,1,""],command:[1,3,1,""],options:[1,3,1,""],run:[1,2,1,""],write_to_file:[1,2,1,""]},"commands.cat_end":{CatEndCommand:[1,1,1,""]},"commands.cat_end.CatEndCommand":{arguments:[1,3,1,""],command:[1,3,1,""],run:[1,2,1,""]},"commands.cd":{CDCommand:[1,1,1,""]},"commands.cd.CDCommand":{arguments:[1,3,1,""],command:[1,3,1,""],run:[1,2,1,""]},"commands.fmap":{FMapCommand:[1,1,1,""]},"commands.fmap.FMapCommand":{command:[1,3,1,""],run:[1,2,1,""]},"commands.hello":{HelloCommand:[1,1,1,""]},"commands.hello.HelloCommand":{command:[1,3,1,""],run:[1,2,1,""]},"commands.ls":{LSCommand:[1,1,1,""]},"commands.ls.LSCommand":{command:[1,3,1,""],run:[1,2,1,""]},"commands.mkdir":{MkDirCommand:[1,1,1,""]},"commands.mkdir.MkDirCommand":{arguments:[1,3,1,""],command:[1,3,1,""],run:[1,2,1,""]},"commands.mv":{MvCommand:[1,1,1,""]},"commands.mv.MvCommand":{arguments:[1,3,1,""],command:[1,3,1,""],run:[1,2,1,""]},"commands.ping":{PingCommand:[1,1,1,""]},"commands.ping.PingCommand":{arguments:[1,3,1,""],command:[1,3,1,""],run:[1,2,1,""]},"commands.pwd":{PWDcommand:[1,1,1,""]},"commands.pwd.PWDcommand":{command:[1,3,1,""],run:[1,2,1,""]},"commands.rm":{RmCommand:[1,1,1,""]},"commands.rm.RmCommand":{arguments:[1,3,1,""],command:[1,3,1,""],options:[1,3,1,""],recursive_remove:[1,2,1,""],run:[1,2,1,""]},"commands.touch":{TouchCommand:[1,1,1,""]},"commands.touch.TouchCommand":{arguments:[1,3,1,""],command:[1,3,1,""],run:[1,2,1,""]},"db.base":{uuid_str:[2,4,1,""]},"db.dao":{directory_dao:[3,0,0,"-"],file_dao:[3,0,0,"-"],sector_dao:[3,0,0,"-"],session_dao:[3,0,0,"-"]},"db.dao.directory_dao":{DirectoryDao:[3,1,1,""]},"db.dao.directory_dao.DirectoryDao":{create_directory:[3,2,1,""],delete_directory:[3,2,1,""],get_directories_from_current_directory:[3,2,1,""],get_directory_from_current_directory:[3,2,1,""],get_root_directory:[3,2,1,""],is_unique_direname:[3,2,1,""],is_valid_dirname:[3,2,1,""]},"db.dao.file_dao":{FileDao:[3,1,1,""]},"db.dao.file_dao.FileDao":{create_file:[3,2,1,""],delete_file:[3,2,1,""],get_all_files:[3,2,1,""],get_file_from_current_directory:[3,2,1,""],get_file_size:[3,2,1,""],get_files_from_current_directory:[3,2,1,""],get_highest_order_of_sectors:[3,2,1,""],get_path:[3,2,1,""],insert_data_in_file:[3,2,1,""],is_unique_filename:[3,2,1,""],is_valid_filename:[3,2,1,""],read_from_file:[3,2,1,""],remove_data_in_file:[3,2,1,""]},"db.dao.sector_dao":{SectorDao:[3,1,1,""]},"db.dao.sector_dao.SectorDao":{create_sector:[3,2,1,""],create_sectors_division:[3,2,1,""],delete_sector:[3,2,1,""],get_first_unused_sector:[3,2,1,""],get_unused_sectors_count:[3,2,1,""],insert_sector_data:[3,2,1,""],is_memory_full:[3,2,1,""]},"db.dao.session_dao":{SessionDao:[3,1,1,""]},"db.dao.session_dao.SessionDao":{create_session:[3,2,1,""],get_last_session:[3,2,1,""]},"db.db":{DB:[2,1,1,""]},"db.db.DB":{connect:[2,2,1,""],session:[2,3,1,""]},"db.models":{directory:[4,0,0,"-"],file:[4,0,0,"-"],sector:[4,0,0,"-"],session:[4,0,0,"-"]},"db.models.directory":{Directory:[4,1,1,""]},"db.models.directory.Directory":{created_at:[4,3,1,""],directory:[4,3,1,""],directory_id:[4,3,1,""],files:[4,3,1,""],id:[4,3,1,""],is_root:[4,3,1,""],name:[4,3,1,""]},"db.models.file":{File:[4,1,1,""]},"db.models.file.File":{created_at:[4,3,1,""],directory_id:[4,3,1,""],id:[4,3,1,""],is_empty:[4,2,1,""],name:[4,3,1,""],sectors:[4,3,1,""]},"db.models.sector":{Sector:[4,1,1,""]},"db.models.sector.Sector":{data:[4,3,1,""],file_id:[4,3,1,""],id:[4,3,1,""],order:[4,3,1,""]},"db.models.session":{Session:[4,1,1,""]},"db.models.session.Session":{created_at:[4,3,1,""],id:[4,3,1,""]},base:{arguments:[0,0,0,"-"],command:[0,0,0,"-"],option:[0,0,0,"-"],terminal:[0,0,0,"-"]},commands:{cat:[1,0,0,"-"],cat_at:[1,0,0,"-"],cat_end:[1,0,0,"-"],cd:[1,0,0,"-"],fmap:[1,0,0,"-"],hello:[1,0,0,"-"],ls:[1,0,0,"-"],mkdir:[1,0,0,"-"],mv:[1,0,0,"-"],ping:[1,0,0,"-"],pwd:[1,0,0,"-"],rm:[1,0,0,"-"],touch:[1,0,0,"-"]},db:{base:[2,0,0,"-"],dao:[3,0,0,"-"],db:[2,0,0,"-"],models:[4,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","attribute","Python attribute"],"4":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:attribute","4":"py:function"},terms:{"char":3,"class":[0,1,2,3,4,7],"new":[1,3,7],"return":[0,1,3,7],"static":[0,3],"true":[0,3],Syed:8,The:[3,9],Used:[1,7],With:[1,7],abc:0,abov:[1,7],access:[0,3],aim:9,alias:1,all:[1,3,7],allow:0,along:[1,7],alreadi:3,api:4,appear:0,append:[1,7],arg1:0,arg2:0,arg:[0,1,7],argument:[1,6,7,9],arif:8,around:0,avail:[3,8,9],avoid:[1,7],babar:8,base:[1,3,4,6,9],baseargu:0,basecommand:[0,1],basetermin:0,below:9,bin:8,brows:9,cat:[6,9],cat_at:[6,7,9],cat_end:[6,7,9],catatcommand:[1,7],catcommand:[1,7],catendcommand:[1,7],cdcommand:[1,7],chang:[1,7],check:[1,7],codebas:8,command:[6,8],commit:3,common:9,connect:2,consol:0,constitu:[1,7],contain:3,content:[6,7,9],context:[0,1,7],contribut:9,count:3,creat:[1,3,7],create_directori:3,create_fil:3,create_sector:3,create_sectors_divis:3,create_sess:3,created_at:4,current:[1,3,7],current_directori:3,dao:[2,6,9],data:[0,3,4],databas:[2,3],db_path:2,declar:4,delet:[1,3,7],delete_directori:3,delete_fil:3,delete_sector:3,desir:[1,7],detail:[1,7],dir_1:[1,7],directori:[0,1,2,3,6,7,9],directory_dao:[2,6],directory_id:4,directory_nam:[1,3,7],directorydao:3,dirnam:3,disk:3,displai:[1,7],distribut:9,document:8,doe:[1,3,7],duplic:[1,7],eesha:8,either:[1,7],emul:9,end:[1,9],enter:[1,7],environ:9,error:[0,1,7],etc:9,execut:0,exist:[0,1,3,7],explor:8,ext:4,fals:0,file:[0,1,2,3,6,7],file_dao:[2,6],file_handl:0,file_id:[3,4],file_nam:[1,7],filedao:3,filenam:[1,3,7],filename1:[1,7],finder:[0,9],first:3,fmap:[6,9],fmapcommand:[1,7],found:0,from:[0,3],full:9,get:8,get_all_fil:3,get_directories_from_current_directori:3,get_directory_from_current_directori:3,get_file_from_current_directori:3,get_file_s:3,get_files_from_current_directori:3,get_first_unused_sector:3,get_highest_order_of_sector:3,get_input:[0,1,7],get_last_sess:3,get_path:3,get_prefix:0,get_root_directori:3,get_unused_sectors_count:3,github:9,given:[1,7],greet:[1,7,9],guid:8,handl:0,have:[0,9],head:9,hello:[6,9],hellocommand:[1,7],hierarchi:9,hold:0,index:[1,3,7,8],input:[0,1,7],insert:3,insert_data_in_fil:3,insert_sector_data:3,insid:[1,3,7],instal:8,intargu:[0,1],integ:0,is_empti:4,is_fil:0,is_memory_ful:3,is_root:4,is_unique_direnam:3,is_unique_filenam:3,is_valid_dirnam:3,is_valid_filenam:3,its:[1,7],kthread:[6,9],kwarg:[0,1,4,7],latest:3,like:[0,9],link:3,linux:9,list:8,locat:[1,7],log:[0,1,7],logic:0,look:0,loop:0,lscommand:[1,7],maaz:8,machin:9,maco:9,main:[6,9],make:[1,7],manag:[0,1,7],manipul:3,map:[1,7],match:0,match_command:0,memori:[1,7],messag:0,mkdir:[6,9],mkdircommand:[1,7],model:[1,2,3,6,7,9],modul:[6,8,9],more:3,most:9,move:[1,7],multi:9,mvcommand:[1,7],name:[1,3,4,7],none:[0,2,3],noth:0,number:3,obj:3,object:[0,1,2,3,7],onc:9,one:[0,1,3,7],option:[1,6,7,9],order:[3,4],out:[1,7],output:[1,7],over:9,overwrit:[1,7],packag:[6,9],page:8,param:[0,1,2,3,7],paramet:0,pars:0,pass:0,path:[0,2],path_to_fil:[1,7],ping:[6,9],pingcommand:[1,7],possibl:3,preced:3,prefix:0,present:[1,7],print:[0,1,7],program:9,project:8,prompt:[0,1,7],properti:[0,4],pwd:[6,9],pwdcommand:[1,7],python:9,rais:[1,7],read:[1,7,9],read_from_fil:3,record:3,recurs:[1,7],recursive_remov:[1,7],remov:[1,3,7],remove_data_in_fil:3,repositori:9,requir:0,reset:0,resid:[1,7],result:0,rmcommand:[1,7],root:3,run:[0,1,7,9],sansio_run:0,search:[1,3,7,8],sector:[2,3,6],sector_dao:[2,6],sector_s:3,sectordao:3,see:[8,9],separ:[0,1,7],session:[2,3,6],session_dao:[2,6],sessiondao:3,set_stdout:0,setup:9,signatur:0,simpl:[1,7],size:[1,3,7],special:3,specif:[1,7],specifi:[0,1,3,7],sqlalchemi:4,sqlite:2,start:[1,2,3,7,8,9],staticargu:0,stdout:0,store:3,string:3,stringargu:[0,1],stringopt:0,submodul:[6,9],subpackag:[6,9],system:[1,7],tabl:4,tahir:8,taken:[1,7],tameez:8,target:[1,7],targetdirectori:[1,7],termin:[1,6,7,9],text:[1,7],thi:[0,1,3,7,8],through:9,total:3,total_s:3,touch:[6,9],touchcommand:[1,7],uniqu:3,usag:[1,7],user:[0,1,7,8],user_input:0,using:0,uuid_str:2,valid:[0,1,3,7],valu:3,welcom:8,well:[1,7],what:9,whatev:[1,7],whether:[0,3],which:[1,7],whole:[1,7],whose:3,within:3,without:[1,7],work:[1,7,9],world:[1,7],wrapper:0,write:[1,7],write_to_fil:1,you:9,your:9},titles:["base package","commands package","db package","db.dao package","db.models package","main module","Distributed-Finder","Available Commands","Operating System CS-330: Distributed Finder","User Guide"],titleterms:{"330":8,argument:0,avail:7,base:[0,2],cat:[1,7],cat_at:1,cat_end:1,codebas:9,command:[0,1,7,9],content:[0,1,2,3,4],dao:3,directori:4,directory_dao:3,distribut:[6,8],end:7,file:4,file_dao:3,finder:[6,8],fmap:[1,7],guid:9,hello:[1,7],indic:8,instal:9,kthread:[1,7],main:5,mkdir:[1,7],model:4,modul:[0,1,2,3,4,5,7],oper:8,option:0,packag:[0,1,2,3,4],ping:[1,7],pwd:[1,7],sector:4,sector_dao:3,session:4,session_dao:3,submodul:[0,1,2,3,4],subpackag:2,system:8,tabl:8,termin:0,touch:[1,7],user:9}})