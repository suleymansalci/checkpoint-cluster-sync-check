# checkpoint-cluster-sync-check
Python script to find cluster synchronization disabled TCP services.   

Some Check Point services could be exempted from clusterXL connection synchronization due to performance considerations like DNS. 

This script checks TCP services for cluster sync option is unchecked. You can modify TCP as UDP if you need to check UDP services. 

There is a default 500 limit per requests. Improvement is needed to find more services.
