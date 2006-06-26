/*******************************************************************************
* mks937aMean.c
* genSub record to calculate the mean pressure from a number of IMGs
*
* Pete Owens
* 26/6/06
*/

#include <vxWorks.h>
#include <types.h>
#include <stdioLib.h>
#include <dbDefs.h>
#include <genSubRecord.h>
#include <dbCommon.h>
#include <dbAccess.h>
#include <recSup.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#ifdef xxxxxxxxxxx
//#include <taskLib.h>

#define MIN(a, b) ((a)<(b)?(a):(b))
//#define WAVE_LOCATIONS 20
//#define WAVE_SIZE 16000

//float *wavestore; /* Global waveform memory storage */
//long datalen[WAVE_LOCATIONS]; /* Global array of waveform lengths */
//long trigStart; /* Global tickount when triggered */
int initialised=FALSE; /* initialised flag */

/////* myRound()
// * Motorola vxWorks BSP doesn't provide round() function, so have
// *  to write our own.
// */
//double myRound(double inval)
//{
//	double fractional,integral;
//
//	fractional=modf(inval,&integral);
//	if (fabs(fractional)<0.5)
//	{
//		return integral;
//	}
//	else
//	{
//		if (inval>0)
//			return integral+1;
//		else
//			return integral-1;
//	}
//}
#endif

/*******************************************************************************
* mks937aMeanInit
* Initialisation function - Does nothing
*/
long mks937aMeanInit (struct genSubRecord *psub)
{
}

/*******************************************************************************
* mks937aMeanCalc
* calculate the mean pressure from a number of IMGs
* Only include IMGs where the status is OK (0 or 1)
*
* Inputs:
* INPA - number of IMGs
*
* Outputs:
* VALA - Mean Pressure
* VALB - Status (0 = OK)
*/
long mks937aMeanCalc (struct genSubRecord *psub)
{
    long n;
    long nImgs;
    double p[10]; /* input pressure */
    double s[10]; /* input status */
 
    /*
    * Extract inputs
    */
    nImgs = (long *) psub->a;
    p[0] = (double *)psub->b;
    p[1] = (double *)psub->c;
    s[0] = (long *)psub->l;
    s[0] = (long *)psub->m;

    *(double *)psub->vala = (p[0] + p[1]) / 2;

    n= nImgs;
    return n;
#ifdef XXXXX
//	long int dest;
//
//	dest = *(long int *)psub->j;
//	datalen[dest] = *(long int *)psub->i;	
//	printf("SIM loading %ld to wave location %ld\n",datalen[dest],dest);
//
//	/* check to make sure that waveform has been downloaded previously */
//	if (wavestore==0)
//	{
//		if((wavestore=malloc(WAVE_SIZE*WAVE_LOCATIONS*sizeof(float)))==NULL)
//		{
//			printf("malloc failed\n");
//			exit(1);
//		}
//		else printf("waveform memory initialised\n");
//	}
//	
//	memcpy(&wavestore[dest*WAVE_SIZE],psub->a,MIN(datalen[dest]*sizeof(float),2000*sizeof(float)));
//	if(datalen[dest]>2000) memcpy(&wavestore[(dest*WAVE_SIZE)+2000],psub->b,MIN((datalen[dest]-2000)*sizeof(float),2000*sizeof(float)));
//	if(datalen[dest]>4000) memcpy(&wavestore[(dest*WAVE_SIZE)+4000],psub->c,MIN((datalen[dest]-4000)*sizeof(float),2000*sizeof(float)));
//	if(datalen[dest]>6000) memcpy(&wavestore[(dest*WAVE_SIZE)+6000],psub->d,MIN((datalen[dest]-6000)*sizeof(float),2000*sizeof(float)));
//	if(datalen[dest]>8000) memcpy(&wavestore[(dest*WAVE_SIZE)+8000],psub->e,MIN((datalen[dest]-8000)*sizeof(float),2000*sizeof(float)));
//	if(datalen[dest]>10000) memcpy(&wavestore[(dest*WAVE_SIZE)+10000],psub->f,MIN((datalen[dest]-10000)*sizeof(float),2000*sizeof(float)));
//	if(datalen[dest]>12000) memcpy(&wavestore[(dest*WAVE_SIZE)+12000],psub->g,MIN((datalen[dest]-12000)*sizeof(float),2000*sizeof(float)));
//	if(datalen[dest]>14000) memcpy(&wavestore[(dest*WAVE_SIZE)+14000],psub->h,MIN((datalen[dest]-14000)*sizeof(float),2000*sizeof(float)));
//
//	printf("SIM-waveform loaded OK\n");
#endif
	return(0);
}
/*******************************************************************************
*/

#ifdef XXXXXXXXXXXXX
/* waveRead()
 * Read back (upload) a waveform from memory
 * 
 */
long waveRead(struct genSubRecord *psub)
{
	long int dest;
	float *data0,*data1,*data2,*data3,*data4,*data5,*data6,*data7;

	dest = *(long int *)psub->b;
	datalen[dest] = *(long int *)psub->a;
	data0=(float*)psub->vala;
	data1=(float*)psub->valb;
	data2=(float*)psub->valc;
	data3=(float*)psub->vald;
	data4=(float*)psub->vale;
	data5=(float*)psub->valf;
	data6=(float*)psub->valg;
	data7=(float*)psub->valh;
	printf("SIM reading %ld from wave location %ld\n",datalen[dest],dest);

	/* check that a waveform has been previously downloaded
	 * Note: could still return all zeros - only checks that a
	 * waveform has been downloaded somewhere, not necessarily in
	 * this sector. */
	if (wavestore==0)
	{
		printf("No waveform at this location.\n");
		return(0);
	}
	
	memcpy(data0,&wavestore[dest*WAVE_SIZE],MIN(datalen[dest]*sizeof(float),2000*sizeof(float)));
	if(datalen[dest]>2000) memcpy(data1,&wavestore[(dest*WAVE_SIZE)+2000],MIN((datalen[dest]-2000)*sizeof(float),2000*sizeof(float)));
	if(datalen[dest]>4000) memcpy(data2,&wavestore[(dest*WAVE_SIZE)+4000],MIN((datalen[dest]-4000)*sizeof(float),2000*sizeof(float)));
	if(datalen[dest]>6000) memcpy(data3,&wavestore[(dest*WAVE_SIZE)+6000],MIN((datalen[dest]-6000)*sizeof(float),2000*sizeof(float)));
	if(datalen[dest]>8000) memcpy(data4,&wavestore[(dest*WAVE_SIZE)+8000],MIN((datalen[dest]-8000)*sizeof(float),2000*sizeof(float)));
	if(datalen[dest]>10000) memcpy(data5,&wavestore[(dest*WAVE_SIZE)+10000],MIN((datalen[dest]-10000)*sizeof(float),2000*sizeof(float)));
	if(datalen[dest]>12000) memcpy(data6,&wavestore[(dest*WAVE_SIZE)+12000],MIN((datalen[dest]-12000)*sizeof(float),2000*sizeof(float)));
	if(datalen[dest]>14000) memcpy(data7,&wavestore[(dest*WAVE_SIZE)+14000],MIN((datalen[dest]-14000)*sizeof(float),2000*sizeof(float)));

	printf("SIM-waveform read OK\n");
	return(0);
}


/* waveTrig()
 * Called when a (software) trigger is received to start the
 * waveform going.
 */
long waveTrig (struct genSubRecord *psub)
{
	trigStart=*(long int*)psub->a;
	printf("wave triggered on count %ld\n",trigStart);
	psub->vala=0;
	return 0;
}


/* waveRun()
 * Return the correct current value given the number of ticks
 * elapsed since the waveform was triggered.
 */
long waveRun (struct genSubRecord *psub)
{  
	int state,simTick,arrayloc;
	long int simCount,elapsed;
	float *arrayval,offset;
	double darrayloc;

	state=*(int*)psub->a;
	simCount=*(long int*)psub->b;
	simTick=*(int*)psub->c;
	offset=*(float*)psub->d;
	arrayval=(float*)psub->vala;

	if(!state)
	{
		/* printf("waveRun skipped - wave not active\n"); */
		*arrayval=offset;
		psub->disa=1;
		return(0);
	}	
	if(trigStart==-1)
	{
		printf("waveRun skipped - no trigger\n");
		psub->disa=1;
		return(0);
	}
	elapsed=simCount-trigStart;
	if (elapsed<0) elapsed=((2^32)-trigStart)+simCount;
	darrayloc=((double)elapsed)/((double)simTick)/0.00008;
	arrayloc=(int)myRound(darrayloc);
	/*printf("arrayloc: %d\n",arrayloc);*/

	if (arrayloc>(datalen[19]-1))
	{
		printf("end of waveform reached.\n");
		trigStart=-1;
		*arrayval=offset;
		psub->disa=1;
	}
	else
	{
		*arrayval=wavestore[(19*WAVE_SIZE)+arrayloc]+offset;
	}
	/*printf("arrayval:%f\n",*arrayval);*/
	return(0);
}
#endif
