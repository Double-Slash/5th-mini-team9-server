-   [API Summary](#api-_)
-   [API Methods - Default](#api-Default)
-   [locationDistrictNameGet](#api-Default-locationDistrictNameGet)
-   [locationGet](#api-Default-locationGet)

Corona Circle API
=================

API and SDK Documentation {#welcome-to-apidoc}
-------------------------

Version: 1.0.0

* * * * *

Corona Circle API

Default
=======

locationDistrictNameGet
=======================

Returns all location where the infected person visited at district

\

``` {.prettyprint .language-html .prettyprinted data-type="get"}
/location/{districtName}
```

### Usage and SDK Samples

-   [Curl](#examples-Default-locationDistrictNameGet-0-curl)
-   [Java](#examples-Default-locationDistrictNameGet-0-java)
-   [Android](#examples-Default-locationDistrictNameGet-0-android)
-   [Obj-C](#examples-Default-locationDistrictNameGet-0-objc)
-   [JavaScript](#examples-Default-locationDistrictNameGet-0-javascript)
-   [C\#](#examples-Default-locationDistrictNameGet-0-csharp)
-   [PHP](#examples-Default-locationDistrictNameGet-0-php)
-   [Perl](#examples-Default-locationDistrictNameGet-0-perl)
-   [Python](#examples-Default-locationDistrictNameGet-0-python)

``` {.prettyprint}
curl -X GET "https://https://220.118.63.34:3000/location/{districtName}"
```

``` {.prettyprint}
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.DefaultApi;

import java.io.File;
import java.util.*;

public class DefaultApiExample {

    public static void main(String[] args) {
        
        DefaultApi apiInstance = new DefaultApi();
        String districtName = districtName_example; // String | 
        try {
            array[Location] result = apiInstance.locationDistrictNameGet(districtName);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DefaultApi#locationDistrictNameGet");
            e.printStackTrace();
        }
    }
}
```

``` {.prettyprint}
import io.swagger.client.api.DefaultApi;

public class DefaultApiExample {

    public static void main(String[] args) {
        DefaultApi apiInstance = new DefaultApi();
        String districtName = districtName_example; // String | 
        try {
            array[Location] result = apiInstance.locationDistrictNameGet(districtName);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DefaultApi#locationDistrictNameGet");
            e.printStackTrace();
        }
    }
}
```

``` {.prettyprint}
String *districtName = districtName_example; // 

DefaultApi *apiInstance = [[DefaultApi alloc] init];

// Returns all location where the infected person visited at district
[apiInstance locationDistrictNameGetWith:districtName
              completionHandler: ^(array[Location] output, NSError* error) {
                            if (output) {
                                NSLog(@"%@", output);
                            }
                            if (error) {
                                NSLog(@"Error: %@", error);
                            }
                        }];
```

``` {.prettyprint}
var CoronaCircleApi = require('corona_circle_api');

var api = new CoronaCircleApi.DefaultApi()

var districtName = districtName_example; // {String} 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.locationDistrictNameGet(districtName, callback);
```

``` {.prettyprint}
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class locationDistrictNameGetExample
    {
        public void main()
        {
            
            var apiInstance = new DefaultApi();
            var districtName = districtName_example;  // String | 

            try
            {
                // Returns all location where the infected person visited at district
                array[Location] result = apiInstance.locationDistrictNameGet(districtName);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.locationDistrictNameGet: " + e.Message );
            }
        }
    }
}
```

``` {.prettyprint}
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\DefaultApi();
$districtName = districtName_example; // String | 

try {
    $result = $api_instance->locationDistrictNameGet($districtName);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->locationDistrictNameGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

``` {.prettyprint}
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::DefaultApi;

my $api_instance = WWW::SwaggerClient::DefaultApi->new();
my $districtName = districtName_example; # String | 

eval { 
    my $result = $api_instance->locationDistrictNameGet(districtName => $districtName);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling DefaultApi->locationDistrictNameGet: $@\n";
}
```

``` {.prettyprint}
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
districtName = districtName_example # String | 

try: 
    # Returns all location where the infected person visited at district
    api_response = api_instance.location_district_name_get(districtName)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->locationDistrictNameGet: %s\n" % e)
```

Parameters
----------

Path parameters

  -------------------------------------------------------------------------
  Name                                 Description
  ------------------------------------ ------------------------------------
  districtName\*                       String
                                       Required
  -------------------------------------------------------------------------

Responses
---------

### Status: 200 - OK

-   [Schema](#responses-locationDistrictNameGet-200-schema)

* * * * *

locationGet
===========

Returns all location where the infected person visited

\

``` {.prettyprint .language-html .prettyprinted data-type="get"}
/location
```

### Usage and SDK Samples

-   [Curl](#examples-Default-locationGet-0-curl)
-   [Java](#examples-Default-locationGet-0-java)
-   [Android](#examples-Default-locationGet-0-android)
-   [Obj-C](#examples-Default-locationGet-0-objc)
-   [JavaScript](#examples-Default-locationGet-0-javascript)
-   [C\#](#examples-Default-locationGet-0-csharp)
-   [PHP](#examples-Default-locationGet-0-php)
-   [Perl](#examples-Default-locationGet-0-perl)
-   [Python](#examples-Default-locationGet-0-python)

``` {.prettyprint}
curl -X GET "https://https://220.118.63.34:3000/location"
```

``` {.prettyprint}
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.DefaultApi;

import java.io.File;
import java.util.*;

public class DefaultApiExample {

    public static void main(String[] args) {
        
        DefaultApi apiInstance = new DefaultApi();
        try {
            array[Location] result = apiInstance.locationGet();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DefaultApi#locationGet");
            e.printStackTrace();
        }
    }
}
```

``` {.prettyprint}
import io.swagger.client.api.DefaultApi;

public class DefaultApiExample {

    public static void main(String[] args) {
        DefaultApi apiInstance = new DefaultApi();
        try {
            array[Location] result = apiInstance.locationGet();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DefaultApi#locationGet");
            e.printStackTrace();
        }
    }
}
```

``` {.prettyprint}
DefaultApi *apiInstance = [[DefaultApi alloc] init];

// Returns all location where the infected person visited
[apiInstance locationGetWithCompletionHandler: 
              ^(array[Location] output, NSError* error) {
                            if (output) {
                                NSLog(@"%@", output);
                            }
                            if (error) {
                                NSLog(@"Error: %@", error);
                            }
                        }];
```

``` {.prettyprint}
var CoronaCircleApi = require('corona_circle_api');

var api = new CoronaCircleApi.DefaultApi()

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.locationGet(callback);
```

``` {.prettyprint}
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class locationGetExample
    {
        public void main()
        {
            
            var apiInstance = new DefaultApi();

            try
            {
                // Returns all location where the infected person visited
                array[Location] result = apiInstance.locationGet();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.locationGet: " + e.Message );
            }
        }
    }
}
```

``` {.prettyprint}
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\DefaultApi();

try {
    $result = $api_instance->locationGet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->locationGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

``` {.prettyprint}
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::DefaultApi;

my $api_instance = WWW::SwaggerClient::DefaultApi->new();

eval { 
    my $result = $api_instance->locationGet();
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling DefaultApi->locationGet: $@\n";
}
```

``` {.prettyprint}
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    # Returns all location where the infected person visited
    api_response = api_instance.location_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->locationGet: %s\n" % e)
```

Parameters
----------

Responses
---------

### Status: 200 - OK

-   [Schema](#responses-locationGet-200-schema)

* * * * *

Suggestions, contact, support and error reporting;

Information URL: [https://helloreverb.com](https://helloreverb.com)

Contact Info: [wang1@hanyang.ac.kr](wang1@hanyang.ac.kr)

MIT

https://opensource.org/licenses/MIT
