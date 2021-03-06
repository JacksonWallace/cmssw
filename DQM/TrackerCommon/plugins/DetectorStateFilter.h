#ifndef DetectorStateFilter_H
#define DetectorStateFilter_H

#include "DataFormats/Scalers/interface/DcsStatus.h"
#include "FWCore/Framework/interface/stream/EDFilter.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class DetectorStateFilter : public edm::stream::EDFilter<> {
public:
  DetectorStateFilter(const edm::ParameterSet &);
  ~DetectorStateFilter() override;

private:
  bool filter(edm::Event &, edm::EventSetup const &) override;

  const bool verbose_;
  uint64_t nEvents_, nSelectedEvents_;
  bool detectorOn_;
  const std::string detectorType_;
  const edm::EDGetTokenT<DcsStatusCollection> dcsStatusLabel_;
};

#endif
