
# 0.1.0
- Generate the api client from the openapi schema

# 0.1.1
- First version in the pip, same as 0.1.0

# 0.1.2
- Adds `_missing_` method to all enums compensating for staffology api bug
where it sends the index of the value instead of the value itself from the enum  
  
# 0.1.3
- Don't return None when there is an error in the api

# 0.1.4
- Fix incorrect response parsing in api exception

# 0.1.5 
- Generate new api client from the openapi schema
- Apply same monkeypatches from previous releases: 
    - Adds `_missing_` method to all enums compensating for staffology api bug
    where it sends the index of the value instead of the value itself from the enum  
    - Don't return None when there is an error in the api
