#ifndef inputMatrixDataColMajor_h
#define inputMatrixDataColMajor_h

#include "inputMatrixData.h"

namespace fp
{

template <typename T, typename Q>
class inputMatrixDataColMajor : public inputMatrixData<T, Q>
{
  public:
	inputMatrixDataColMajor(const T *Xmat, const Q *Yvec, int numObs, int numFeatures) : inputMatrixData<T, Q>(Xmat, Yvec, numObs, numFeatures)
	{
	}

	inline T returnFeatureValue(const int &featureNum,
								const int &observationNum)
	{
		return this->inputXData[this->numObs * featureNum + observationNum];
	}

	inline void prefetchFeatureValue(const int &featureNum,
									 const int &observationNum)
	{
		__builtin_prefetch(&this->inputXData[this->numObs * featureNum + observationNum], 0, 1);
	}
};

} // namespace fp
#endif // inputMatrixDataColMajor_h
