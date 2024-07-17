window.pdocSearch=function(){!function(){function t(t){if(null===t||"object"!=typeof t)return t;var e=t.constructor();for(var i in t)t.hasOwnProperty(i)&&(e[i]=t[i]);return e}var e=function(t){var i=new e.Index;return i.pipeline.add(e.trimmer,e.stopWordFilter,e.stemmer),t&&t.call(i,i),i};e.version="0.9.5",lunr=e,e.utils={},e.utils.warn=function(t){return function(e){t.console&&console.warn&&console.warn(e)}}(this),e.utils.toString=function(t){return null==t?"":t.toString()},e.EventEmitter=function(){this.events={}},e.EventEmitter.prototype.addListener=function(){var t=Array.prototype.slice.call(arguments),e=t.pop(),i=t;if("function"!=typeof e)throw new TypeError("last argument must be a function");i.forEach(function(t){this.hasHandler(t)||(this.events[t]=[]),this.events[t].push(e)},this)},e.EventEmitter.prototype.removeListener=function(t,e){if(this.hasHandler(t)){var i=this.events[t].indexOf(e);-1!==i&&(this.events[t].splice(i,1),0==this.events[t].length&&delete this.events[t])}},e.EventEmitter.prototype.emit=function(t){if(this.hasHandler(t)){var e=Array.prototype.slice.call(arguments,1);this.events[t].forEach(function(t){t.apply(void 0,e)},this)}},e.EventEmitter.prototype.hasHandler=function(t){return t in this.events},e.tokenizer=function(t){if(!arguments.length||null==t)return[];if(Array.isArray(t)){var i=t.filter(function(t){return null!=t});i=i.map(function(t){return e.utils.toString(t).toLowerCase()});var o=[];return i.forEach(function(t){var i=t.split(e.tokenizer.seperator);o=o.concat(i)},this),o}return t.toString().trim().toLowerCase().split(e.tokenizer.seperator)},e.tokenizer.defaultSeperator=/[\s\-]+/,e.tokenizer.seperator=e.tokenizer.defaultSeperator,e.tokenizer.setSeperator=function(t){null!=t&&"object"==typeof t&&(e.tokenizer.seperator=t)},e.tokenizer.resetSeperator=function(){e.tokenizer.seperator=e.tokenizer.defaultSeperator},e.tokenizer.getSeperator=function(){return e.tokenizer.seperator},e.Pipeline=function(){this._queue=[]},e.Pipeline.registeredFunctions={},e.Pipeline.registerFunction=function(t,i){i in e.Pipeline.registeredFunctions&&e.utils.warn("Overwriting existing registered function: "+i),t.label=i,e.Pipeline.registeredFunctions[i]=t},e.Pipeline.getRegisteredFunction=function(t){return t in e.Pipeline.registeredFunctions!=1?null:e.Pipeline.registeredFunctions[t]},e.Pipeline.warnIfFunctionNotRegistered=function(t){t.label&&t.label in this.registeredFunctions||e.utils.warn("Function is not registered with pipeline. This may cause problems when serialising the index.\n",t)},e.Pipeline.load=function(t){var i=new e.Pipeline;return t.forEach(function(t){var o=e.Pipeline.getRegisteredFunction(t);if(!o)throw new Error("Cannot load un-registered function: "+t);i.add(o)}),i},e.Pipeline.prototype.add=function(){Array.prototype.slice.call(arguments).forEach(function(t){e.Pipeline.warnIfFunctionNotRegistered(t),this._queue.push(t)},this)},e.Pipeline.prototype.after=function(t,i){e.Pipeline.warnIfFunctionNotRegistered(i);var o=this._queue.indexOf(t);if(-1===o)throw new Error("Cannot find existingFn");this._queue.splice(o+1,0,i)},e.Pipeline.prototype.before=function(t,i){e.Pipeline.warnIfFunctionNotRegistered(i);var o=this._queue.indexOf(t);if(-1===o)throw new Error("Cannot find existingFn");this._queue.splice(o,0,i)},e.Pipeline.prototype.remove=function(t){var e=this._queue.indexOf(t);-1!==e&&this._queue.splice(e,1)},e.Pipeline.prototype.run=function(t){for(var e=[],i=t.length,o=this._queue.length,s=0;i>s;s++){for(var n=t[s],d=0;o>d&&null!=(n=this._queue[d](n,s,t));d++);null!=n&&e.push(n)}return e},e.Pipeline.prototype.reset=function(){this._queue=[]},e.Pipeline.prototype.get=function(){return this._queue},e.Pipeline.prototype.toJSON=function(){return this._queue.map(function(t){return e.Pipeline.warnIfFunctionNotRegistered(t),t.label})},e.Index=function(){this._fields=[],this._ref="id",this.pipeline=new e.Pipeline,this.documentStore=new e.DocumentStore,this.index={},this.eventEmitter=new e.EventEmitter,this._idfCache={},this.on("add","remove","update",function(){this._idfCache={}}.bind(this))},e.Index.prototype.on=function(){var t=Array.prototype.slice.call(arguments);return this.eventEmitter.addListener.apply(this.eventEmitter,t)},e.Index.prototype.off=function(t,e){return this.eventEmitter.removeListener(t,e)},e.Index.load=function(t){t.version!==e.version&&e.utils.warn("version mismatch: current "+e.version+" importing "+t.version);var i=new this;for(var o in i._fields=t.fields,i._ref=t.ref,i.documentStore=e.DocumentStore.load(t.documentStore),i.pipeline=e.Pipeline.load(t.pipeline),i.index={},t.index)i.index[o]=e.InvertedIndex.load(t.index[o]);return i},e.Index.prototype.addField=function(t){return this._fields.push(t),this.index[t]=new e.InvertedIndex,this},e.Index.prototype.setRef=function(t){return this._ref=t,this},e.Index.prototype.saveDocument=function(t){return this.documentStore=new e.DocumentStore(t),this},e.Index.prototype.addDoc=function(t,i){if(t){i=void 0===i||i;var o=t[this._ref];this.documentStore.addDoc(o,t),this._fields.forEach(function(i){var s=this.pipeline.run(e.tokenizer(t[i]));this.documentStore.addFieldLength(o,i,s.length);var n={};for(var d in s.forEach(function(t){t in n?n[t]+=1:n[t]=1},this),n){var r=n[d];r=Math.sqrt(r),this.index[i].addToken(d,{ref:o,tf:r})}},this),i&&this.eventEmitter.emit("add",t,this)}},e.Index.prototype.removeDocByRef=function(t){if(t&&!1!==this.documentStore.isDocStored()&&this.documentStore.hasDoc(t)){var e=this.documentStore.getDoc(t);this.removeDoc(e,!1)}},e.Index.prototype.removeDoc=function(t,i){if(t){i=void 0===i||i;var o=t[this._ref];this.documentStore.hasDoc(o)&&(this.documentStore.removeDoc(o),this._fields.forEach(function(i){this.pipeline.run(e.tokenizer(t[i])).forEach(function(t){this.index[i].removeToken(t,o)},this)},this),i&&this.eventEmitter.emit("remove",t,this))}},e.Index.prototype.updateDoc=function(t,e){e=void 0===e||e;this.removeDocByRef(t[this._ref],!1),this.addDoc(t,!1),e&&this.eventEmitter.emit("update",t,this)},e.Index.prototype.idf=function(t,e){var i="@"+e+"/"+t;if(Object.prototype.hasOwnProperty.call(this._idfCache,i))return this._idfCache[i];var o=this.index[e].getDocFreq(t),s=1+Math.log(this.documentStore.length/(o+1));return this._idfCache[i]=s,s},e.Index.prototype.getFields=function(){return this._fields.slice()},e.Index.prototype.search=function(t,i){if(!t)return[];t="string"==typeof t?{any:t}:JSON.parse(JSON.stringify(t));var o=null;null!=i&&(o=JSON.stringify(i));for(var s=new e.Configuration(o,this.getFields()).get(),n={},d=Object.keys(t),r=0;r<d.length;r++){var f=d[r];n[f]=this.pipeline.run(e.tokenizer(t[f]))}var a={};for(var p in s){var c=n[p]||n.any;if(c){var u=this.fieldSearch(c,p,s),l=s[p].boost;for(var g in u)u[g]=u[g]*l;for(var g in u)g in a?a[g]+=u[g]:a[g]=u[g]}}var h,m=[];for(var g in a)h={ref:g,score:a[g]},this.documentStore.hasDoc(g)&&(h.doc=this.documentStore.getDoc(g)),m.push(h);return m.sort(function(t,e){return e.score-t.score}),m},e.Index.prototype.fieldSearch=function(t,e,i){var o=i[e].bool,s=i[e].expand,n=i[e].boost,d=null,r={};return 0!==n?(t.forEach(function(t){var i=[t];1==s&&(i=this.index[e].expandToken(t));var n={};i.forEach(function(i){var s=this.index[e].getDocs(i),f=this.idf(i,e);if(d&&"AND"==o){var a={};for(var p in d)p in s&&(a[p]=s[p]);s=a}for(var p in i==t&&this.fieldSearchStats(r,i,s),s){var c=this.index[e].getTermFrequency(i,p),u=this.documentStore.getFieldLength(p,e),l=1;0!=u&&(l=1/Math.sqrt(u));var g=1;i!=t&&(g=.15*(1-(i.length-t.length)/i.length));var h=c*f*l*g;p in n?n[p]+=h:n[p]=h}},this),d=this.mergeScores(d,n,o)},this),d=this.coordNorm(d,r,t.length)):void 0},e.Index.prototype.mergeScores=function(t,e,i){if(!t)return e;if("AND"==i){var o={};for(var s in e)s in t&&(o[s]=t[s]+e[s]);return o}for(var s in e)s in t?t[s]+=e[s]:t[s]=e[s];return t},e.Index.prototype.fieldSearchStats=function(t,e,i){for(var o in i)o in t?t[o].push(e):t[o]=[e]},e.Index.prototype.coordNorm=function(t,e,i){for(var o in t)if(o in e){var s=e[o].length;t[o]=t[o]*s/i}return t},e.Index.prototype.toJSON=function(){var t={};return this._fields.forEach(function(e){t[e]=this.index[e].toJSON()},this),{version:e.version,fields:this._fields,ref:this._ref,documentStore:this.documentStore.toJSON(),index:t,pipeline:this.pipeline.toJSON()}},e.Index.prototype.use=function(t){var e=Array.prototype.slice.call(arguments,1);e.unshift(this),t.apply(this,e)},e.DocumentStore=function(t){this._save=null==t||t,this.docs={},this.docInfo={},this.length=0},e.DocumentStore.load=function(t){var e=new this;return e.length=t.length,e.docs=t.docs,e.docInfo=t.docInfo,e._save=t.save,e},e.DocumentStore.prototype.isDocStored=function(){return this._save},e.DocumentStore.prototype.addDoc=function(e,i){this.hasDoc(e)||this.length++,this.docs[e]=!0===this._save?t(i):null},e.DocumentStore.prototype.getDoc=function(t){return!1===this.hasDoc(t)?null:this.docs[t]},e.DocumentStore.prototype.hasDoc=function(t){return t in this.docs},e.DocumentStore.prototype.removeDoc=function(t){this.hasDoc(t)&&(delete this.docs[t],delete this.docInfo[t],this.length--)},e.DocumentStore.prototype.addFieldLength=function(t,e,i){null!=t&&0!=this.hasDoc(t)&&(this.docInfo[t]||(this.docInfo[t]={}),this.docInfo[t][e]=i)},e.DocumentStore.prototype.updateFieldLength=function(t,e,i){null!=t&&0!=this.hasDoc(t)&&this.addFieldLength(t,e,i)},e.DocumentStore.prototype.getFieldLength=function(t,e){return null==t?0:t in this.docs&&e in this.docInfo[t]?this.docInfo[t][e]:0},e.DocumentStore.prototype.toJSON=function(){return{docs:this.docs,docInfo:this.docInfo,length:this.length,save:this._save}},e.stemmer=function(){var t={ational:"ate",tional:"tion",enci:"ence",anci:"ance",izer:"ize",bli:"ble",alli:"al",entli:"ent",eli:"e",ousli:"ous",ization:"ize",ation:"ate",ator:"ate",alism:"al",iveness:"ive",fulness:"ful",ousness:"ous",aliti:"al",iviti:"ive",biliti:"ble",logi:"log"},e={icate:"ic",ative:"",alize:"al",iciti:"ic",ical:"ic",ful:"",ness:""},i="[aeiouy]",o="[^aeiou]"+"[^aeiouy]*",s=i+"[aeiou]*",n="^("+o+")?"+s+o+"("+s+")?$",d="^("+o+")?"+s+o+s+o,r="^("+o+")?"+i,f=new RegExp("^("+o+")?"+s+o),a=new RegExp(d),p=new RegExp(n),c=new RegExp(r),u=/^(.+?)(ss|i)es$/,l=/^(.+?)([^s])s$/,g=/^(.+?)eed$/,h=/^(.+?)(ed|ing)$/,m=/.$/,v=/(at|bl|iz)$/,y=new RegExp("([^aeiouylsz])\\1$"),x=new RegExp("^"+o+i+"[^aeiouwxy]$"),w=/^(.+?[^aeiou])y$/,b=/^(.+?)(ational|tional|enci|anci|izer|bli|alli|entli|eli|ousli|ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti|logi)$/,S=/^(.+?)(icate|ative|alize|iciti|ical|ful|ness)$/,I=/^(.+?)(al|ance|ence|er|ic|able|ible|ant|ement|ment|ent|ou|ism|ate|iti|ous|ive|ize)$/,k=/^(.+?)(s|t)(ion)$/,F=/^(.+?)e$/,_=/ll$/,E=new RegExp("^"+o+i+"[^aeiouwxy]$");return function(i){var o,s,n,d,r,D,q;if(i.length<3)return i;if("y"==(n=i.substr(0,1))&&(i=n.toUpperCase()+i.substr(1)),r=l,(d=u).test(i)?i=i.replace(d,"$1$2"):r.test(i)&&(i=i.replace(r,"$1$2")),r=h,(d=g).test(i)){var P=d.exec(i);(d=f).test(P[1])&&(d=m,i=i.replace(d,""))}else if(r.test(i)){o=(P=r.exec(i))[1],(r=c).test(o)&&(i=o,D=y,q=x,(r=v).test(i)?i+="e":D.test(i)?(d=m,i=i.replace(d,"")):q.test(i)&&(i+="e"))}(d=w).test(i)&&(i=(o=(P=d.exec(i))[1])+"i");(d=b).test(i)&&(o=(P=d.exec(i))[1],s=P[2],(d=f).test(o)&&(i=o+t[s]));(d=S).test(i)&&(o=(P=d.exec(i))[1],s=P[2],(d=f).test(o)&&(i=o+e[s]));if(r=k,(d=I).test(i))o=(P=d.exec(i))[1],(d=a).test(o)&&(i=o);else if(r.test(i)){o=(P=r.exec(i))[1]+P[2],(r=a).test(o)&&(i=o)}(d=F).test(i)&&(o=(P=d.exec(i))[1],r=p,D=E,((d=a).test(o)||r.test(o)&&!D.test(o))&&(i=o));return r=a,(d=_).test(i)&&r.test(i)&&(d=m,i=i.replace(d,"")),"y"==n&&(i=n.toLowerCase()+i.substr(1)),i}}(),e.Pipeline.registerFunction(e.stemmer,"stemmer"),e.stopWordFilter=function(t){return t&&!0!==e.stopWordFilter.stopWords[t]?t:void 0},e.clearStopWords=function(){e.stopWordFilter.stopWords={}},e.addStopWords=function(t){null!=t&&!1!==Array.isArray(t)&&t.forEach(function(t){e.stopWordFilter.stopWords[t]=!0},this)},e.resetStopWords=function(){e.stopWordFilter.stopWords=e.defaultStopWords},e.defaultStopWords={"":!0,a:!0,able:!0,about:!0,across:!0,after:!0,all:!0,almost:!0,also:!0,am:!0,among:!0,an:!0,and:!0,any:!0,are:!0,as:!0,at:!0,be:!0,because:!0,been:!0,but:!0,by:!0,can:!0,cannot:!0,could:!0,dear:!0,did:!0,"do":!0,does:!0,either:!0,"else":!0,ever:!0,every:!0,"for":!0,from:!0,get:!0,got:!0,had:!0,has:!0,have:!0,he:!0,her:!0,hers:!0,him:!0,his:!0,how:!0,however:!0,i:!0,"if":!0,"in":!0,into:!0,is:!0,it:!0,its:!0,just:!0,least:!0,"let":!0,like:!0,likely:!0,may:!0,me:!0,might:!0,most:!0,must:!0,my:!0,neither:!0,no:!0,nor:!0,not:!0,of:!0,off:!0,often:!0,on:!0,only:!0,or:!0,other:!0,our:!0,own:!0,rather:!0,said:!0,say:!0,says:!0,she:!0,should:!0,since:!0,so:!0,some:!0,than:!0,that:!0,the:!0,their:!0,them:!0,then:!0,there:!0,these:!0,they:!0,"this":!0,tis:!0,to:!0,too:!0,twas:!0,us:!0,wants:!0,was:!0,we:!0,were:!0,what:!0,when:!0,where:!0,which:!0,"while":!0,who:!0,whom:!0,why:!0,will:!0,"with":!0,would:!0,yet:!0,you:!0,your:!0},e.stopWordFilter.stopWords=e.defaultStopWords,e.Pipeline.registerFunction(e.stopWordFilter,"stopWordFilter"),e.trimmer=function(t){if(null==t)throw new Error("token should not be undefined");return t.replace(/^\W+/,"").replace(/\W+$/,"")},e.Pipeline.registerFunction(e.trimmer,"trimmer"),e.InvertedIndex=function(){this.root={docs:{},df:0}},e.InvertedIndex.load=function(t){var e=new this;return e.root=t.root,e},e.InvertedIndex.prototype.addToken=function(t,e,i){i=i||this.root;for(var o=0;o<=t.length-1;){var s=t[o];s in i||(i[s]={docs:{},df:0}),o+=1,i=i[s]}var n=e.ref;i.docs[n]?i.docs[n]={tf:e.tf}:(i.docs[n]={tf:e.tf},i.df+=1)},e.InvertedIndex.prototype.hasToken=function(t){if(!t)return!1;for(var e=this.root,i=0;i<t.length;i++){if(!e[t[i]])return!1;e=e[t[i]]}return!0},e.InvertedIndex.prototype.getNode=function(t){if(!t)return null;for(var e=this.root,i=0;i<t.length;i++){if(!e[t[i]])return null;e=e[t[i]]}return e},e.InvertedIndex.prototype.getDocs=function(t){var e=this.getNode(t);return null==e?{}:e.docs},e.InvertedIndex.prototype.getTermFrequency=function(t,e){var i=this.getNode(t);return null==i?0:e in i.docs?i.docs[e].tf:0},e.InvertedIndex.prototype.getDocFreq=function(t){var e=this.getNode(t);return null==e?0:e.df},e.InvertedIndex.prototype.removeToken=function(t,e){if(t){var i=this.getNode(t);null!=i&&e in i.docs&&(delete i.docs[e],i.df-=1)}},e.InvertedIndex.prototype.expandToken=function(t,e,i){if(null==t||""==t)return[];e=e||[];if(null==i&&null==(i=this.getNode(t)))return e;for(var o in i.df>0&&e.push(t),i)"docs"!==o&&"df"!==o&&this.expandToken(t+o,e,i[o]);return e},e.InvertedIndex.prototype.toJSON=function(){return{root:this.root}},e.Configuration=function(t,i){var o;t=t||"";if(null==i||null==i)throw new Error("fields should not be null");this.config={};try{o=JSON.parse(t),this.buildUserConfig(o,i)}catch(s){e.utils.warn("user configuration parse failed, will use default configuration"),this.buildDefaultConfig(i)}},e.Configuration.prototype.buildDefaultConfig=function(t){this.reset(),t.forEach(function(t){this.config[t]={boost:1,bool:"OR",expand:!1}},this)},e.Configuration.prototype.buildUserConfig=function(t,i){var o="OR",s=!1;if(this.reset(),"bool"in t&&(o=t.bool||o),"expand"in t&&(s=t.expand||s),"fields"in t)for(var n in t.fields)if(i.indexOf(n)>-1){var d=t.fields[n],r=s;null!=d.expand&&(r=d.expand),this.config[n]={boost:d.boost||0===d.boost?d.boost:1,bool:d.bool||o,expand:r}}else e.utils.warn("field name in user configuration not found in index instance fields");else this.addAllFields2UserConfig(o,s,i)},e.Configuration.prototype.addAllFields2UserConfig=function(t,e,i){i.forEach(function(i){this.config[i]={boost:1,bool:t,expand:e}},this)},e.Configuration.prototype.get=function(){return this.config},e.Configuration.prototype.reset=function(){this.config={}},lunr.SortedSet=function(){this.length=0,this.elements=[]},lunr.SortedSet.load=function(t){var e=new this;return e.elements=t,e.length=t.length,e},lunr.SortedSet.prototype.add=function(){var t,e;for(t=0;t<arguments.length;t++)e=arguments[t],~this.indexOf(e)||this.elements.splice(this.locationFor(e),0,e);this.length=this.elements.length},lunr.SortedSet.prototype.toArray=function(){return this.elements.slice()},lunr.SortedSet.prototype.map=function(t,e){return this.elements.map(t,e)},lunr.SortedSet.prototype.forEach=function(t,e){return this.elements.forEach(t,e)},lunr.SortedSet.prototype.indexOf=function(t){for(var e=0,i=this.elements.length,o=i-e,s=e+Math.floor(o/2),n=this.elements[s];o>1;){if(n===t)return s;t>n&&(e=s),n>t&&(i=s),o=i-e,s=e+Math.floor(o/2),n=this.elements[s]}return n===t?s:-1},lunr.SortedSet.prototype.locationFor=function(t){for(var e=0,i=this.elements.length,o=i-e,s=e+Math.floor(o/2),n=this.elements[s];o>1;)t>n&&(e=s),n>t&&(i=s),o=i-e,s=e+Math.floor(o/2),n=this.elements[s];return n>t?s:t>n?s+1:void 0},lunr.SortedSet.prototype.intersect=function(t){for(var e=new lunr.SortedSet,i=0,o=0,s=this.length,n=t.length,d=this.elements,r=t.elements;!(i>s-1||o>n-1);)d[i]!==r[o]?d[i]<r[o]?i++:d[i]>r[o]&&o++:(e.add(d[i]),i++,o++);return e},lunr.SortedSet.prototype.clone=function(){var t=new lunr.SortedSet;return t.elements=this.toArray(),t.length=t.elements.length,t},lunr.SortedSet.prototype.union=function(t){var e,i,o;this.length>=t.length?(e=this,i=t):(e=t,i=this),o=e.clone();for(var s=0,n=i.toArray();s<n.length;s++)o.add(n[s]);return o},lunr.SortedSet.prototype.toJSON=function(){return this.toArray()},function(t,e){"function"==typeof define&&define.amd?define(e):"object"==typeof exports?module.exports=e():t.elasticlunr=e()}(this,function(){return e})}();const t={version:"0.9.5",fields:["qualname","fullname","annotation","default_value","signature","bases","doc"],ref:"fullname",documentStore:{docs:{"apis.gui":{fullname:"apis.gui",modulename:"apis.gui",kind:"module",doc:"<p></p>\n"},"apis.gui.app":{fullname:"apis.gui.app",modulename:"apis.gui",qualname:"app",kind:"variable",doc:"<p></p>\n",default_value:"None"},"apis.gui.textbox":{fullname:"apis.gui.textbox",modulename:"apis.gui",qualname:"textbox",kind:"variable",doc:"<p></p>\n",default_value:"None"},"apis.gui.clear":{fullname:"apis.gui.clear",modulename:"apis.gui",qualname:"clear",kind:"function",doc:'<p>This allows us to "clear" text from the textbox on the GUI.</p>\n\n<h6 id="returns">Returns:</h6>\n\n<blockquote>\n  <p><code>None</code> but instead updates the GUI\'s textbox appropriately.</p>\n</blockquote>\n',signature:'<span class="signature pdoc-code condensed">(<span class="return-annotation">):</span></span>',funcdef:"def"},"apis.gui.print":{fullname:"apis.gui.print",modulename:"apis.gui",qualname:"print",kind:"function",doc:'<p>This allows us to "print" text to the textbox on the GUI.</p>\n\n<h6 id="arguments">Arguments:</h6>\n\n<ul>\n<li><strong>txt (<code>str</code>):</strong>  whatever text you\'d like printed to the screen (note: like the <code>print</code> function you can give it as many inputs as you\'d like!)</li>\n<li><strong>sep (<code>str</code>):</strong>  default separator to be used with multiple text arguments (like <code>print</code>)</li>\n<li><strong>end (<code>str</code>):</strong>  default ending character to be used (like <code>print</code>)</li>\n</ul>\n\n<h6 id="returns">Returns:</h6>\n\n<blockquote>\n  <p><code>None</code> but instead updates the GUI\'s textbox appropriately.</p>\n</blockquote>\n',signature:'<span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">txt</span>, </span><span class="param"><span class="n">sep</span><span class="o">=</span><span class="s1">&#39; &#39;</span>, </span><span class="param"><span class="n">end</span><span class="o">=</span><span class="s1">&#39;</span><span class="se">\\n</span><span class="s1">&#39;</span></span><span class="return-annotation">):</span></span>',funcdef:"def"},"apis.gui.popup":{fullname:"apis.gui.popup",modulename:"apis.gui",qualname:"popup",kind:"function",doc:'<p>This allows us to create a pop-up a window without any prompt.</p>\n\n<h6 id="arguments">Arguments:</h6>\n\n<ul>\n<li><strong>message (<code>str</code>):</strong>  whatever text you\'d like to be shown in the pop-up window.</li>\n<li><strong>title (<code>str</code>):</strong>  the title of the window.</li>\n<li><strong>kind (<code>str</code>):</strong>  Either <code>"info"</code>, <code>"warning"</code>, or <code>"error"</code>. Just changes the icon in the pop-up.</li>\n</ul>\n\n<h6 id="returns">Returns:</h6>\n\n<blockquote>\n  <p><code>None</code> just shows the window.</p>\n</blockquote>\n',signature:'<span class="signature pdoc-code condensed">(<span class="param"><span class="n">message</span><span class="p">:</span> <span class="nb">str</span>, </span><span class="param"><span class="n">title</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;Pop-Up&#39;</span>, </span><span class="param"><span class="n">kind</span><span class="o">=</span><span class="s1">&#39;info&#39;</span></span><span class="return-annotation">):</span></span>',funcdef:"def"},"apis.gui.input":{fullname:"apis.gui.input",modulename:"apis.gui",qualname:"input",kind:"function",doc:'<p>This allows us to ask for "input" from our GUI. It pops-up a window with a given prompt.</p>\n\n<h6 id="arguments">Arguments:</h6>\n\n<ul>\n<li><strong>prompt (<code>str</code>):</strong>  whatever text you\'d like to be shown in the pop-up window.</li>\n</ul>\n\n<h6 id="returns">Returns:</h6>\n\n<blockquote>\n  <p>a <code>str</code> containing what the user typed in the pop-up window. If they didn\'t enter anything or if they clicked Cancel it will return <code>None</code>.</p>\n</blockquote>\n',signature:'<span class="signature pdoc-code condensed">(<span class="param"><span class="n">prompt</span><span class="o">=</span><span class="s1">&#39;&#39;</span></span><span class="return-annotation">):</span></span>',funcdef:"def"}},docInfo:{"apis.gui":{qualname:0,fullname:2,annotation:0,default_value:0,signature:0,bases:0,doc:3},"apis.gui.app":{qualname:1,fullname:3,annotation:0,default_value:1,signature:0,bases:0,doc:3},"apis.gui.textbox":{qualname:1,fullname:3,annotation:0,default_value:1,signature:0,bases:0,doc:3},"apis.gui.clear":{qualname:1,fullname:3,annotation:0,default_value:0,signature:7,bases:0,doc:36},"apis.gui.print":{qualname:1,fullname:3,annotation:0,default_value:0,signature:44,bases:0,doc:123},"apis.gui.popup":{qualname:1,fullname:3,annotation:0,default_value:0,signature:52,bases:0,doc:113},"apis.gui.input":{qualname:1,fullname:3,annotation:0,default_value:0,signature:19,bases:0,doc:93}},length:7,save:!0},index:{qualname:{root:{docs:{},df:0,a:{docs:{},df:0,p:{docs:{},df:0,p:{docs:{"apis.gui.app":{tf:1}},df:1}}},t:{docs:{},df:0,e:{docs:{},df:0,x:{docs:{},df:0,t:{docs:{},df:0,b:{docs:{},df:0,o:{docs:{},df:0,x:{docs:{"apis.gui.textbox":{tf:1}},df:1}}}}}}},c:{docs:{},df:0,l:{docs:{},df:0,e:{docs:{},df:0,a:{docs:{},df:0,r:{docs:{"apis.gui.clear":{tf:1}},df:1}}}}},p:{docs:{},df:0,r:{docs:{},df:0,i:{docs:{},df:0,n:{docs:{},df:0,t:{docs:{"apis.gui.print":{tf:1}},df:1}}}},o:{docs:{},df:0,p:{docs:{},df:0,u:{docs:{},df:0,p:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}},i:{docs:{},df:0,n:{docs:{},df:0,p:{docs:{},df:0,u:{docs:{},df:0,t:{docs:{"apis.gui.input":{tf:1}},df:1}}}}}}},fullname:{root:{docs:{},df:0,a:{docs:{},df:0,p:{docs:{},df:0,i:{docs:{},df:0,s:{docs:{"apis.gui":{tf:1},"apis.gui.app":{tf:1},"apis.gui.textbox":{tf:1},"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:7}},p:{docs:{"apis.gui.app":{tf:1}},df:1}}},g:{docs:{},df:0,u:{docs:{},df:0,i:{docs:{"apis.gui":{tf:1},"apis.gui.app":{tf:1},"apis.gui.textbox":{tf:1},"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:7}}},t:{docs:{},df:0,e:{docs:{},df:0,x:{docs:{},df:0,t:{docs:{},df:0,b:{docs:{},df:0,o:{docs:{},df:0,x:{docs:{"apis.gui.textbox":{tf:1}},df:1}}}}}}},c:{docs:{},df:0,l:{docs:{},df:0,e:{docs:{},df:0,a:{docs:{},df:0,r:{docs:{"apis.gui.clear":{tf:1}},df:1}}}}},p:{docs:{},df:0,r:{docs:{},df:0,i:{docs:{},df:0,n:{docs:{},df:0,t:{docs:{"apis.gui.print":{tf:1}},df:1}}}},o:{docs:{},df:0,p:{docs:{},df:0,u:{docs:{},df:0,p:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}},i:{docs:{},df:0,n:{docs:{},df:0,p:{docs:{},df:0,u:{docs:{},df:0,t:{docs:{"apis.gui.input":{tf:1}},df:1}}}}}}},annotation:{root:{docs:{},df:0}},default_value:{root:{docs:{},df:0,n:{docs:{},df:0,o:{docs:{},df:0,n:{docs:{},df:0,e:{docs:{"apis.gui.app":{tf:1},"apis.gui.textbox":{tf:1}},df:2}}}}}},signature:{root:{3:{9:{docs:{"apis.gui.print":{tf:2},"apis.gui.popup":{tf:2},"apis.gui.input":{tf:1.4142135623730951}},df:3},docs:{},df:0},docs:{"apis.gui.clear":{tf:2.6457513110645907},"apis.gui.print":{tf:6},"apis.gui.popup":{tf:6.324555320336759},"apis.gui.input":{tf:4}},df:4,t:{docs:{},df:0,x:{docs:{},df:0,t:{docs:{"apis.gui.print":{tf:1}},df:1}},i:{docs:{},df:0,t:{docs:{},df:0,l:{docs:{},df:0,e:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}},s:{docs:{},df:0,e:{docs:{},df:0,p:{docs:{"apis.gui.print":{tf:1}},df:1}},t:{docs:{},df:0,r:{docs:{"apis.gui.popup":{tf:1.4142135623730951}},df:1}}},e:{docs:{},df:0,n:{docs:{},df:0,d:{docs:{"apis.gui.print":{tf:1}},df:1}}},n:{docs:{"apis.gui.print":{tf:1}},df:1},m:{docs:{},df:0,e:{docs:{},df:0,s:{docs:{},df:0,s:{docs:{},df:0,a:{docs:{},df:0,g:{docs:{},df:0,e:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}}}},p:{docs:{},df:0,o:{docs:{},df:0,p:{docs:{"apis.gui.popup":{tf:1}},df:1}},r:{docs:{},df:0,o:{docs:{},df:0,m:{docs:{},df:0,p:{docs:{},df:0,t:{docs:{"apis.gui.input":{tf:1}},df:1}}}}}},u:{docs:{},df:0,p:{docs:{"apis.gui.popup":{tf:1}},df:1}},k:{docs:{},df:0,i:{docs:{},df:0,n:{docs:{},df:0,d:{docs:{"apis.gui.popup":{tf:1}},df:1}}}},i:{docs:{},df:0,n:{docs:{},df:0,f:{docs:{},df:0,o:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}}},bases:{root:{docs:{},df:0}},doc:{root:{docs:{"apis.gui":{tf:1.7320508075688772},"apis.gui.app":{tf:1.7320508075688772},"apis.gui.textbox":{tf:1.7320508075688772},"apis.gui.clear":{tf:3.7416573867739413},"apis.gui.print":{tf:7.0710678118654755},"apis.gui.popup":{tf:7.483314773547883},"apis.gui.input":{tf:5.477225575051661}},df:7,t:{docs:{"apis.gui.input":{tf:1}},df:1,h:{docs:{},df:0,i:{docs:{},df:0,s:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:4}},e:{docs:{"apis.gui.clear":{tf:1.7320508075688772},"apis.gui.print":{tf:2.23606797749979},"apis.gui.popup":{tf:2.449489742783178},"apis.gui.input":{tf:1.7320508075688772}},df:4,y:{docs:{"apis.gui.input":{tf:1.4142135623730951}},df:1}}},o:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:2.23606797749979},"apis.gui.popup":{tf:1.4142135623730951},"apis.gui.input":{tf:1.4142135623730951}},df:4},e:{docs:{},df:0,x:{docs:{},df:0,t:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1.7320508075688772},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:4,b:{docs:{},df:0,o:{docs:{},df:0,x:{docs:{"apis.gui.clear":{tf:1.4142135623730951},"apis.gui.print":{tf:1.4142135623730951}},df:2}}}}}},x:{docs:{},df:0,t:{docs:{"apis.gui.print":{tf:1}},df:1}},i:{docs:{},df:0,t:{docs:{},df:0,l:{docs:{},df:0,e:{docs:{"apis.gui.popup":{tf:1.4142135623730951}},df:1}}}},y:{docs:{},df:0,p:{docs:{},df:0,e:{docs:{},df:0,d:{docs:{"apis.gui.input":{tf:1}},df:1}}}}},a:{docs:{"apis.gui.popup":{tf:1.4142135623730951},"apis.gui.input":{tf:1.7320508075688772}},df:2,l:{docs:{},df:0,l:{docs:{},df:0,o:{docs:{},df:0,w:{docs:{},df:0,s:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:4}}}}},p:{docs:{},df:0,p:{docs:{},df:0,r:{docs:{},df:0,o:{docs:{},df:0,p:{docs:{},df:0,r:{docs:{},df:0,i:{docs:{},df:0,a:{docs:{},df:0,t:{docs:{},df:0,e:{docs:{},df:0,l:{docs:{},df:0,y:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1}},df:2}}}}}}}}}}}},r:{docs:{},df:0,g:{docs:{},df:0,u:{docs:{},df:0,m:{docs:{},df:0,e:{docs:{},df:0,n:{docs:{},df:0,t:{docs:{},df:0,s:{docs:{"apis.gui.print":{tf:1.4142135623730951},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:3}}}}}}}},s:{docs:{"apis.gui.print":{tf:1.4142135623730951}},df:1,k:{docs:{"apis.gui.input":{tf:1}},df:1}},n:{docs:{},df:0,y:{docs:{"apis.gui.popup":{tf:1}},df:1,t:{docs:{},df:0,h:{docs:{},df:0,i:{docs:{},df:0,n:{docs:{},df:0,g:{docs:{"apis.gui.input":{tf:1}},df:1}}}}}}}},u:{docs:{},df:0,s:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:4,e:{docs:{},df:0,d:{docs:{"apis.gui.print":{tf:1.4142135623730951}},df:1},r:{docs:{"apis.gui.input":{tf:1}},df:1}}},p:{docs:{"apis.gui.popup":{tf:1.7320508075688772},"apis.gui.input":{tf:1.7320508075688772}},df:2,d:{docs:{},df:0,a:{docs:{},df:0,t:{docs:{},df:0,e:{docs:{},df:0,s:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1}},df:2}}}}}}},c:{docs:{},df:0,l:{docs:{},df:0,e:{docs:{},df:0,a:{docs:{},df:0,r:{docs:{"apis.gui.clear":{tf:1}},df:1}}},i:{docs:{},df:0,c:{docs:{},df:0,k:{docs:{},df:0,e:{docs:{},df:0,d:{docs:{"apis.gui.input":{tf:1}},df:1}}}}}},a:{docs:{},df:0,n:{docs:{"apis.gui.print":{tf:1}},df:1,c:{docs:{},df:0,e:{docs:{},df:0,l:{docs:{"apis.gui.input":{tf:1}},df:1}}}}},h:{docs:{},df:0,a:{docs:{},df:0,r:{docs:{},df:0,a:{docs:{},df:0,c:{docs:{},df:0,t:{docs:{},df:0,e:{docs:{},df:0,r:{docs:{"apis.gui.print":{tf:1}},df:1}}}}}},n:{docs:{},df:0,g:{docs:{},df:0,e:{docs:{},df:0,s:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}}},r:{docs:{},df:0,e:{docs:{},df:0,a:{docs:{},df:0,t:{docs:{},df:0,e:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}},o:{docs:{},df:0,n:{docs:{},df:0,t:{docs:{},df:0,a:{docs:{},df:0,i:{docs:{},df:0,n:{docs:{},df:0,i:{docs:{},df:0,n:{docs:{},df:0,g:{docs:{"apis.gui.input":{tf:1}},df:1}}}}}}}}}},f:{docs:{},df:0,r:{docs:{},df:0,o:{docs:{},df:0,m:{docs:{"apis.gui.clear":{tf:1},"apis.gui.input":{tf:1}},df:2}}},u:{docs:{},df:0,n:{docs:{},df:0,c:{docs:{},df:0,t:{docs:{},df:0,i:{docs:{},df:0,o:{docs:{},df:0,n:{docs:{"apis.gui.print":{tf:1}},df:1}}}}}}},o:{docs:{},df:0,r:{docs:{"apis.gui.input":{tf:1}},df:1}}},o:{docs:{},df:0,n:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1}},df:2},f:{docs:{"apis.gui.popup":{tf:1}},df:1},r:{docs:{"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:2},u:{docs:{},df:0,r:{docs:{"apis.gui.input":{tf:1}},df:1}}},g:{docs:{},df:0,u:{docs:{},df:0,i:{docs:{"apis.gui.clear":{tf:1.4142135623730951},"apis.gui.print":{tf:1.4142135623730951},"apis.gui.input":{tf:1}},df:3}},i:{docs:{},df:0,v:{docs:{},df:0,e:{docs:{"apis.gui.print":{tf:1}},df:1,n:{docs:{"apis.gui.input":{tf:1}},df:1}}}}},r:{docs:{},df:0,e:{docs:{},df:0,t:{docs:{},df:0,u:{docs:{},df:0,r:{docs:{},df:0,n:{docs:{"apis.gui.input":{tf:1}},df:1,s:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:4}}}}}}},n:{docs:{},df:0,o:{docs:{},df:0,n:{docs:{},df:0,e:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:4}},t:{docs:{},df:0,e:{docs:{"apis.gui.print":{tf:1}},df:1}}}},b:{docs:{},df:0,u:{docs:{},df:0,t:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1}},df:2}},e:{docs:{"apis.gui.print":{tf:1.4142135623730951},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:3}},i:{docs:{},df:0,n:{docs:{"apis.gui.popup":{tf:1.4142135623730951},"apis.gui.input":{tf:1.4142135623730951}},df:2,s:{docs:{},df:0,t:{docs:{},df:0,e:{docs:{},df:0,a:{docs:{},df:0,d:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1}},df:2}}}}},p:{docs:{},df:0,u:{docs:{},df:0,t:{docs:{"apis.gui.input":{tf:1}},df:1,s:{docs:{"apis.gui.print":{tf:1}},df:1}}}},f:{docs:{},df:0,o:{docs:{"apis.gui.popup":{tf:1}},df:1}}},t:{docs:{"apis.gui.print":{tf:1},"apis.gui.input":{tf:1.4142135623730951}},df:2},c:{docs:{},df:0,o:{docs:{},df:0,n:{docs:{"apis.gui.popup":{tf:1}},df:1}}},f:{docs:{"apis.gui.input":{tf:1.4142135623730951}},df:1}},s:{docs:{"apis.gui.clear":{tf:1},"apis.gui.print":{tf:1}},df:2,t:{docs:{},df:0,r:{docs:{"apis.gui.print":{tf:1.7320508075688772},"apis.gui.popup":{tf:1.7320508075688772},"apis.gui.input":{tf:1.4142135623730951}},df:3}},c:{docs:{},df:0,r:{docs:{},df:0,e:{docs:{},df:0,e:{docs:{},df:0,n:{docs:{"apis.gui.print":{tf:1}},df:1}}}}},e:{docs:{},df:0,p:{docs:{"apis.gui.print":{tf:1}},df:1,a:{docs:{},df:0,r:{docs:{},df:0,a:{docs:{},df:0,t:{docs:{},df:0,o:{docs:{},df:0,r:{docs:{"apis.gui.print":{tf:1}},df:1}}}}}}}},h:{docs:{},df:0,o:{docs:{},df:0,w:{docs:{},df:0,n:{docs:{"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:2},s:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}},p:{docs:{},df:0,r:{docs:{},df:0,i:{docs:{},df:0,n:{docs:{},df:0,t:{docs:{"apis.gui.print":{tf:2}},df:1,e:{docs:{},df:0,d:{docs:{"apis.gui.print":{tf:1}},df:1}}}}},o:{docs:{},df:0,m:{docs:{},df:0,p:{docs:{},df:0,t:{docs:{"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1.4142135623730951}},df:2}}}}},o:{docs:{},df:0,p:{docs:{"apis.gui.popup":{tf:1.7320508075688772},
"apis.gui.input":{tf:1.4142135623730951}},df:2,s:{docs:{"apis.gui.input":{tf:1}},df:1}}}},w:{docs:{},df:0,h:{docs:{},df:0,a:{docs:{},df:0,t:{docs:{"apis.gui.input":{tf:1}},df:1,e:{docs:{},df:0,v:{docs:{},df:0,e:{docs:{},df:0,r:{docs:{"apis.gui.print":{tf:1},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:3}}}}}}},i:{docs:{},df:0,t:{docs:{},df:0,h:{docs:{"apis.gui.print":{tf:1},"apis.gui.input":{tf:1}},df:2,o:{docs:{},df:0,u:{docs:{},df:0,t:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}},n:{docs:{},df:0,d:{docs:{},df:0,o:{docs:{},df:0,w:{docs:{"apis.gui.popup":{tf:2},"apis.gui.input":{tf:1.7320508075688772}},df:2}}}},l:{docs:{},df:0,l:{docs:{"apis.gui.input":{tf:1}},df:1}}},a:{docs:{},df:0,r:{docs:{},df:0,n:{docs:{},df:0,i:{docs:{},df:0,n:{docs:{},df:0,g:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}}}},y:{docs:{},df:0,o:{docs:{},df:0,u:{docs:{"apis.gui.print":{tf:1.7320508075688772},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:3}}},d:{docs:{"apis.gui.print":{tf:1.4142135623730951},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:3,e:{docs:{},df:0,f:{docs:{},df:0,a:{docs:{},df:0,u:{docs:{},df:0,l:{docs:{},df:0,t:{docs:{"apis.gui.print":{tf:1.4142135623730951}},df:1}}}}}},i:{docs:{},df:0,d:{docs:{},df:0,n:{docs:{"apis.gui.input":{tf:1}},df:1}}}},l:{docs:{},df:0,i:{docs:{},df:0,k:{docs:{},df:0,e:{docs:{"apis.gui.print":{tf:2.23606797749979},"apis.gui.popup":{tf:1},"apis.gui.input":{tf:1}},df:3}}}},m:{docs:{},df:0,a:{docs:{},df:0,n:{docs:{},df:0,y:{docs:{"apis.gui.print":{tf:1}},df:1}}},u:{docs:{},df:0,l:{docs:{},df:0,t:{docs:{},df:0,i:{docs:{},df:0,p:{docs:{},df:0,l:{docs:{},df:0,e:{docs:{"apis.gui.print":{tf:1}},df:1}}}}}}},e:{docs:{},df:0,s:{docs:{},df:0,s:{docs:{},df:0,a:{docs:{},df:0,g:{docs:{},df:0,e:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}}}},e:{docs:{},df:0,n:{docs:{},df:0,d:{docs:{"apis.gui.print":{tf:1}},df:1,i:{docs:{},df:0,n:{docs:{},df:0,g:{docs:{"apis.gui.print":{tf:1}},df:1}}}},t:{docs:{},df:0,e:{docs:{},df:0,r:{docs:{"apis.gui.input":{tf:1}},df:1}}}},i:{docs:{},df:0,t:{docs:{},df:0,h:{docs:{},df:0,e:{docs:{},df:0,r:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}},r:{docs:{},df:0,r:{docs:{},df:0,o:{docs:{},df:0,r:{docs:{"apis.gui.popup":{tf:1}},df:1}}}}},k:{docs:{},df:0,i:{docs:{},df:0,n:{docs:{},df:0,d:{docs:{"apis.gui.popup":{tf:1}},df:1}}}},j:{docs:{},df:0,u:{docs:{},df:0,s:{docs:{},df:0,t:{docs:{"apis.gui.popup":{tf:1.4142135623730951}},df:1}}}}}}},pipeline:["trimmer"],_isPrebuiltIndex:!0};let e;if(elasticlunr.tokenizer.setSeperator(/[\s\-.;&_'"=,()]+|<[^>]*>/),t._isPrebuiltIndex)console.info("using precompiled search index"),e=elasticlunr.Index.load(t);else{console.time("building search index"),e=elasticlunr(function(){this.pipeline.remove(elasticlunr.stemmer),this.pipeline.remove(elasticlunr.stopWordFilter),this.addField("qualname"),this.addField("fullname"),this.addField("annotation"),this.addField("default_value"),this.addField("signature"),this.addField("bases"),this.addField("doc"),this.setRef("fullname")});for(let i of t)e.addDoc(i);console.timeEnd("building search index")}return t=>e.search(t,{fields:{qualname:{boost:4},fullname:{boost:2},annotation:{boost:2},default_value:{boost:2},signature:{boost:2},bases:{boost:2},doc:{boost:1}},expand:!0})}();