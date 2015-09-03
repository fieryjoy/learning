#include "dbg.h" 
#include "static.h"

int main()
{
	log_info("Hello %d", hello());
	log_info("Hello %d", hello());	
	log_info("Hello %d", hello());	

	log_info("from hello count is %d", *pcount);
	return 0;
}
