(function ( $ ) {
    "use strict";
    var sparqler = new SPARQL.Service("http://linkedgeodata.org/sparql");
    sparqler.setOutput("json");
    sparqler.setMethod("GET");
    sparqler.addDefaultGraph("http://linkedgeodata.org");
    sparqler.setPrefix("lgdo", "http://linkedgeodata.org/ontology/"); 
    sparqler.setPrefix("fn", "http://www.w3.org/2005/xpath-functions#");
    sparqler.setPrefix("geo", "http://www.w3.org/2003/01/geo/wgs84_pos#");

    $(function(){
        var sparql_template = Handlebars.compile($('#rando-rest-query').html()),
            resturant_template = Handlebars.compile($('#restaurant-template').html()),
            resturant_place_holder = $('#restuarants-placeholder')

        sparqler.query(
            sparql_template({
                "date": new Date().toDateString()
            }),
            {
                "success": function(data){
                    resturant_place_holder.html(
                        resturant_template({
                            "restaurants" : data["results"]["bindings"]
                        })
                    );
                    console.log(                        resturant_template({
                            "restaurants" : data["results"]["bindings"]
                        }));
                },
                "failure": function(){
                    debugger;
                }
            }
        )
    });
}( jQuery ));