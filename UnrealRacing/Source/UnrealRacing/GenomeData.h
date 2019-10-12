// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "EvaluationState.h"

#include "CoreMinimal.h"
#include "UObject/NoExportTypes.h"
#include "GenomeData.generated.h"

/**
 * 
 */
UCLASS(BlueprintType)
class UNREALRACING_API UGenomeData : public UObject
{
	GENERATED_BODY()

public:

	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	int genomeID;
	
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	float fitness = 0;

	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	bool shouldMutate = false;

	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	EEvaluationState evaluationState = EEvaluationState::Ready;
	
};
