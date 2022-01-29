# cisco-phone-ad-xml-book
python connector to active directory . Returns  XML  format for cisco  phones  , this is  working concept
# usage
http://127.0.0.1:5000/search?department=search_att_value  (you can search any attribute in your AD)

Returns 
```<CiscoIPPhoneDirectory>
  <Prompt>Records 1 to 4 of 4</Prompt>
    <DirectoryEntry>
      <Name>Bahruz Y</Name>
      <Telephone>1131</Telephone>
    </DirectoryEntry>
    <DirectoryEntry>
      <Name>Emin F</Name>
      <Telephone>1060</Telephone>
    </DirectoryEntry>
</CiscoIPPhoneDirectory> 
      
