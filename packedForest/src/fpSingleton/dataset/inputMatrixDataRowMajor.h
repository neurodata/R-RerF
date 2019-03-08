#ifndef inputMatrixDataRowMajor_h
#define inputMatrixDataRowMajor_h

#include "inputMatrixData.h"

namespace fp
{

template <typename T, typename Q>
class inputMatrixDataRowMajor : public inputMatrixData<T, Q>
{
  public:
    inputMatrixDataRowMajor(const T *Xmat, const Q *Yvec, int numObs, int numFeatures) : inputMatrixData<T, Q>(Xmat, Yvec, numObs, numFeatures)
    {
    }

    inline T returnFeatureValue(const int &featureNum,
                                const int &observationNum)
    {
        return this->inputXData[observationNum * this->numFeatures + featureNum];
    }

    inline void prefetchFeatureValue(const int &featureNum,
                                     const int &observationNum)
    {
        __builtin_prefetch(&this->inputXData[observationNum * this->numFeatures + featureNum], 0, 1);
    }
};
} // namespace fp
#endif // inputMatrixDataRowMajor_h
